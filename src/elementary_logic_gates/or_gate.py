from .not_gate import NotGate
from .and_gate import AndGate


class OrGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def __call__(self, a: int, b: int) -> int:
        """
        Truth table for OR gate:
        | A | B | NOT(A) | NOT(B) | NOT(A) AND NOT(B) | NOT(NOT(A) AND NOT(B)) | Q |
        |---|---|--------|--------|-------------------|------------------------|---|
        | 0 | 0 | 1      | 1      | 1                 | 0                      | 0 |
        | 0 | 1 | 1      | 0      | 0                 | 1                      | 1 |
        | 1 | 0 | 0      | 1      | 0                 | 1                      | 1 |
        | 1 | 1 | 0      | 0      | 0                 | 1                      | 1 |
        """
        not_a: int = self.not_gate(a)
        not_b: int = self.not_gate(b)
        not_a_and_not_b: int = self.and_gate(not_a, not_b)
        return self.not_gate(not_a_and_not_b)
