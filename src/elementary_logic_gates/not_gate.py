from .nand_gate import NandGate


class NotGate:
    def __init__(self):
        self.nand_gate = NandGate()

    def __call__(self, a: int) -> int:
        """
        Truth table for NOT gate:
        | A | Q |
        |---|---|
        | 0 | 1 |
        | 1 | 0 |
        """

        return int(self.nand_gate(a, a))
