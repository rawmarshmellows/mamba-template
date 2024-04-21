from .mux16_gate import Mux16Gate
from src.types.bits import Bits2, Bits16


class Mux4Way16Gate:
    def __init__(self):
        self.mux16_gate = Mux16Gate()

    def __call__(
        self, a: Bits16, b: Bits16, c: Bits16, d: Bits16, sel: Bits2
    ) -> Bits16:
        return self.mux16_gate(
            self.mux16_gate(a, c, sel[0]), self.mux16_gate(b, d, sel[0]), sel[1]
        )
