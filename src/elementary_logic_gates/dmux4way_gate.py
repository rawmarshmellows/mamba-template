from .dmux_gate import DmuxGate
from src.types.bits import Bit, Bits2, Bits4


class Dmux4WayGate:
    def __init__(self):
        self.dmux_gate = DmuxGate()

    def __call__(self, input_bit: Bit, sel: Bits2) -> Bits4:
        x0, x1 = self.dmux_gate(input_bit, sel[0])

        a, b = self.dmux_gate(x0, sel[1])
        c, d = self.dmux_gate(x1, sel[1])
        return Bits4.from_bits([a, b, c, d])
