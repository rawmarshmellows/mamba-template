from .mux_gate import MuxGate
from src.types.bits import Bit, Bits16


class Mux16Gate:
    def __init__(self):
        self.mux_gate = MuxGate()

    def __call__(self, a: Bits16, b: Bits16, sel: Bit) -> Bits16:
        return Bits16.from_bits(
            [
                self.mux_gate(a[0], b[0], sel),
                self.mux_gate(a[1], b[1], sel),
                self.mux_gate(a[2], b[2], sel),
                self.mux_gate(a[3], b[3], sel),
                self.mux_gate(a[4], b[4], sel),
                self.mux_gate(a[5], b[5], sel),
                self.mux_gate(a[6], b[6], sel),
                self.mux_gate(a[7], b[7], sel),
                self.mux_gate(a[8], b[8], sel),
                self.mux_gate(a[9], b[9], sel),
                self.mux_gate(a[10], b[10], sel),
                self.mux_gate(a[11], b[11], sel),
                self.mux_gate(a[12], b[12], sel),
                self.mux_gate(a[13], b[13], sel),
                self.mux_gate(a[14], b[14], sel),
                self.mux_gate(a[15], b[15], sel),
            ]
        )
