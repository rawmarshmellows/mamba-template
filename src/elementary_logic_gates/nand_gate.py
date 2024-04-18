class NandGate:
    def __call__(self, a: int, b: int) -> int:
        """
        Truth table for NAND gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 1 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 0 |
        """
        return int(not (a and b))
