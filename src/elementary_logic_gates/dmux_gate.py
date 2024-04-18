from .and_gate import AndGate
from .not_gate import NotGate
from .or_gate import OrGate


class DmuxGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()
        self.or_gate = OrGate()

    def __call__(self, a: int, sel: int) -> tuple[int, int]:
        """
        Truth table for DMUX gate:
        | A  | SEL | X | Y |
        | 0  | 0   | 0 | 0 |
        | 0  | 1   | 0 | 0 |
        | 1  | 0   | 1 | 0 |
        | 1  | 1   | 0 | 1 |
        """
        not_sel = self.not_gate(sel)

        a1sel0x1 = self.and_gate(a, not_sel)
        a0sel1y1 = self.and_gate(a, sel)

        return a1sel0x1, a0sel1y1
