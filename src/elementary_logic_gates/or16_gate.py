from .or_gate import OrGate
from src.types.bits import Bits16


class Or16Gate:
    def __init__(self):
        self.or_gate = OrGate()

    def __call__(self, a_bits_16: Bits16, b_bits_16) -> Bits16:
        return Bits16.from_bits(
            [
                self.or_gate(a_bits_16[0], b_bits_16[0]),
                self.or_gate(a_bits_16[1], b_bits_16[1]),
                self.or_gate(a_bits_16[2], b_bits_16[2]),
                self.or_gate(a_bits_16[3], b_bits_16[3]),
                self.or_gate(a_bits_16[4], b_bits_16[4]),
                self.or_gate(a_bits_16[5], b_bits_16[5]),
                self.or_gate(a_bits_16[6], b_bits_16[6]),
                self.or_gate(a_bits_16[7], b_bits_16[7]),
                self.or_gate(a_bits_16[8], b_bits_16[8]),
                self.or_gate(a_bits_16[9], b_bits_16[9]),
                self.or_gate(a_bits_16[10], b_bits_16[10]),
                self.or_gate(a_bits_16[11], b_bits_16[11]),
                self.or_gate(a_bits_16[12], b_bits_16[12]),
                self.or_gate(a_bits_16[13], b_bits_16[13]),
                self.or_gate(a_bits_16[14], b_bits_16[14]),
                self.or_gate(a_bits_16[15], b_bits_16[15]),
            ]
        )
