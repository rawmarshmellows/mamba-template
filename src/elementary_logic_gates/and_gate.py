from .nand_gate import NandGate
from .not_gate import NotGate


class AndGate:
    def __init__(self):
        self.nand_gate = NandGate()
        self.not_gate = NotGate()

    def __call__(self, a: int, b: int) -> int:
        """
        Truth table for AND gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 0 |
        | 0 | 1 | 0 |
        | 1 | 0 | 0 |
        | 1 | 1 | 1 |
        """
        return int(self.not_gate(self.nand_gate(a, b)))
