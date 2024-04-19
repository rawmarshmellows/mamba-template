from .nand_gate import NandGate
from .not_gate import NotGate
from src.types.bits import Bit


class AndGate:
    def __init__(self):
        self.nand_gate = NandGate()
        self.not_gate = NotGate()

    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for AND gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 0 |
        | 0 | 1 | 0 |
        | 1 | 0 | 0 |
        | 1 | 1 | 1 |
        """
        return self.not_gate(self.nand_gate(a, b))
