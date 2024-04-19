from .and_gate import AndGate
from src.types.bits import Bits16


class And16Gate:
    def __init__(self):
        self.and_gate = AndGate()

    def __call__(self, a_bits_16: Bits16, b_bits_16) -> Bits16:
        return Bits16.from_bits(
            [
                self.and_gate(a_bits_16[0], b_bits_16[0]),
                self.and_gate(a_bits_16[1], b_bits_16[1]),
                self.and_gate(a_bits_16[2], b_bits_16[2]),
                self.and_gate(a_bits_16[3], b_bits_16[3]),
                self.and_gate(a_bits_16[4], b_bits_16[4]),
                self.and_gate(a_bits_16[5], b_bits_16[5]),
                self.and_gate(a_bits_16[6], b_bits_16[6]),
                self.and_gate(a_bits_16[7], b_bits_16[7]),
                self.and_gate(a_bits_16[8], b_bits_16[8]),
                self.and_gate(a_bits_16[9], b_bits_16[9]),
                self.and_gate(a_bits_16[10], b_bits_16[10]),
                self.and_gate(a_bits_16[11], b_bits_16[11]),
                self.and_gate(a_bits_16[12], b_bits_16[12]),
                self.and_gate(a_bits_16[13], b_bits_16[13]),
                self.and_gate(a_bits_16[14], b_bits_16[14]),
                self.and_gate(a_bits_16[15], b_bits_16[15]),
            ]
        )
