from .mux16_gate import Mux16Gate
from .mux4way16_gate import Mux4Way16Gate
from src.types.bits import Bits3, Bits16


class Mux8Way16Gate:
    def __init__(self):
        self.mux16_gate = Mux16Gate()
        self.mux4way16_gate = Mux4Way16Gate()

    def __call__(
        self,
        a: Bits16,
        b: Bits16,
        c: Bits16,
        d: Bits16,
        e: Bits16,
        f: Bits16,
        g: Bits16,
        h: Bits16,
        sel: Bits3,
    ) -> Bits16:
        aceg_mux4way16 = self.mux4way16_gate(a, c, e, g, [sel[0], sel[1]])
        bdfh_mux4way16 = self.mux4way16_gate(b, d, f, h, [sel[0], sel[1]])
        return self.mux16_gate(aceg_mux4way16, bdfh_mux4way16, sel[2])
