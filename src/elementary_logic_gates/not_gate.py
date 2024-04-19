from .nand_gate import NandGate
from src.types.bits import Bit


class NotGate:
    def __init__(self):
        self.nand_gate = NandGate()

    def __call__(self, a: Bit) -> Bit:
        """
        Truth table for NOT gate:
        | A | Q |
        |---|---|
        | 0 | 1 |
        | 1 | 0 |
        """

        return self.nand_gate(a, a)
