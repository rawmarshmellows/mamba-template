from .not_gate import NotGate
from src.types.bits import Bits16


class Not16Gate:
    def __init__(self):
        self.not_gate = NotGate()

    def __call__(self, bits_16: Bits16) -> Bits16:
        return Bits16.from_bits(
            [
                self.not_gate(bits_16[0]),
                self.not_gate(bits_16[1]),
                self.not_gate(bits_16[2]),
                self.not_gate(bits_16[3]),
                self.not_gate(bits_16[4]),
                self.not_gate(bits_16[5]),
                self.not_gate(bits_16[6]),
                self.not_gate(bits_16[7]),
                self.not_gate(bits_16[8]),
                self.not_gate(bits_16[9]),
                self.not_gate(bits_16[10]),
                self.not_gate(bits_16[11]),
                self.not_gate(bits_16[12]),
                self.not_gate(bits_16[13]),
                self.not_gate(bits_16[14]),
                self.not_gate(bits_16[15]),
            ]
        )
