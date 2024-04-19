from .and_gate import AndGate
from .not_gate import NotGate
from .or_gate import OrGate
from src.types.bits import Bit


class XorGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()
        self.or_gate = OrGate()

    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for XOR gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 0 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 0 |
        """
        a0b1q1: Bit = self.and_gate(self.not_gate(a), b)
        a1b0q1: Bit = self.and_gate(a, self.not_gate(b))
        return self.or_gate(a0b1q1, a1b0q1)
