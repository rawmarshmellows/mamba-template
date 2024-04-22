from src.elementary_logic_gates.xor_gate import XorGate
from src.elementary_logic_gates.and_gate import AndGate
from src.types.bits import Bit, Bits2


class HalfAdderChip:
    def __init__(self):
        self.xor_gate = XorGate()
        self.and_gate = AndGate()

    def __call__(self, a: Bit, b: Bit) -> Bits2:
        """
        The truth table for the Half Adder chip is as follows:
        | A | B | SUM | CARRY |
        | 0 | 0 | 0   | 0     |
        | 0 | 1 | 1   | 0     |
        | 1 | 0 | 1   | 0     |
        | 1 | 1 | 0   | 1     |
        """
        return Bits2.from_bits([self.xor_gate(a, b), self.and_gate(a, b)])
