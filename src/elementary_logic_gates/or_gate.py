from .not_gate import NotGate
from .and_gate import AndGate
from src.types.bits import Bit


class OrGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for OR gate:
        | A | B | NOT(A) | NOT(B) | NOT(A) AND NOT(B) | NOT(NOT(A) AND NOT(B)) | Q |
        |---|---|--------|--------|-------------------|------------------------|---|
        | 0 | 0 | 1      | 1      | 1                 | 0                      | 0 |
        | 0 | 1 | 1      | 0      | 0                 | 1                      | 1 |
        | 1 | 0 | 0      | 1      | 0                 | 1                      | 1 |
        | 1 | 1 | 0      | 0      | 0                 | 1                      | 1 |
        """
        not_a: Bit = self.not_gate(a)
        not_b: Bit = self.not_gate(b)
        not_a_and_not_b: Bit = self.and_gate(not_a, not_b)
        return self.not_gate(not_a_and_not_b)
