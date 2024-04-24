from .add16_chip import Add16Chip
from .inc16_chip import Inc16Chip
from src.types.bits import Bits16, Bits8, Bit
from src.types.alu import ALUOutput
from src.elementary_logic_gates.not_gate import NotGate
from src.elementary_logic_gates.mux16_gate import Mux16Gate
from src.elementary_logic_gates.not16_gate import Not16Gate
from src.elementary_logic_gates.and16_gate import And16Gate
from src.elementary_logic_gates.or_gate import OrGate
from src.elementary_logic_gates.or8way_gate import Or8WayGate


class ALUChip:
    def __init__(self):
        self.not_gate = NotGate()
        self.or_gate = OrGate()
        self.or8way_gate = Or8WayGate()
        self.mux16_gate = Mux16Gate()
        self.not16_gate = Not16Gate()
        self.and16_gate = And16Gate()
        self.add16_chip = Add16Chip()
        self.inc16_chip = Inc16Chip()

    def __call__(
        self, x: Bits16, y: Bits16, zx: Bit, nx: Bit, zy: Bit, ny: Bit, f: Bit, no: Bit
    ) -> ALUOutput:
        """
        x: 16-bit input
        y: 16-bit input
        zx: If zx == 1, replace x with 0
        nx: If nx == 1, ~x
        zy: If zy == 1, replace y with 0
        ny: If ny == 1, ~y
        f:  If f == 1, compute (x + y)
            If f == 0, compute (x & y)
        no: If no == 1, compute ~result
        out: 16-bit output
        zr: If out == 0, set to 1
        ng: If out < 0, set to 1
        """
        x = self.mux16_gate(x, Bits16.from_string("0000000000000000"), sel=zx)
        x = self.mux16_gate(x, self.not16_gate(x), sel=nx)

        y = self.mux16_gate(y, Bits16.from_string("0000000000000000"), sel=zy)
        y = self.mux16_gate(y, self.not16_gate(y), sel=ny)

        out = self.mux16_gate(self.and16_gate(x, y), self.add16_chip(x, y), sel=f)
        out = self.mux16_gate(out, self.not16_gate(out), sel=no)

        zr = self.not_gate(
            self.or_gate(
                self.or8way_gate(Bits8.from_bits(out[:8])),
                self.or8way_gate(Bits8.from_bits(out[8:])),
            )
        )
        ng = out[0]
        return ALUOutput(out=out, zr=zr, ng=ng)
