from .or_gate import OrGate
from src.types.bits import Bit, Bits8


class Or8WayGate:
    def __init__(self):
        self.or_gate = OrGate()

    def __call__(self, bits_8: Bits8) -> Bit:
        return self.or_gate(
            self.or_gate(
                self.or_gate(bits_8[0], bits_8[1]),
                self.or_gate(bits_8[2], bits_8[3]),
            ),
            self.or_gate(
                self.or_gate(bits_8[4], bits_8[5]),
                self.or_gate(bits_8[6], bits_8[7]),
            ),
        )
