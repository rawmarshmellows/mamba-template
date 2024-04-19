from src.types.bits import Bit


class NandGate:
    def __call__(self, a: Bit, b: Bit) -> Bit:
        """
        Truth table for NAND gate:
        | A | B | Q |
        |---|---|---|
        | 0 | 0 | 1 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 0 |
        """
        assert type(a) == Bit, f"Invalid input a: {a} for NAND gate."
        assert type(b) == Bit, f"Invalid input b: {b} for NAND gate."

        if a == Bit(0) and b == Bit(0):
            return Bit(1)
        if a == Bit(0) and b == Bit(1):
            return Bit(1)
        if a == Bit(1) and b == Bit(0):
            return Bit(1)
        if a == Bit(1) and b == Bit(1):
            return Bit(0)
        raise ValueError(f"Invalid input a: {a}, b: {b} for NAND gate.")
