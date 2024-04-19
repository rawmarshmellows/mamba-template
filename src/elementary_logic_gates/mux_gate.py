from .and_gate import AndGate
from .not_gate import NotGate
from .or_gate import OrGate
from src.types.bits import Bit


class MuxGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()
        self.or_gate = OrGate()

    def __call__(self, a: Bit, b: Bit, sel: Bit) -> Bit:
        """
        Truth table for MUX gate:
        | A | B | SEL | Q |
        |---|---|-----|---|
        | 0 | 0 | 0   | 0 |
        | 0 | 0 | 1   | 0 |
        | 0 | 1 | 0   | 0 |
        | 0 | 1 | 1   | 1 |
        | 1 | 0 | 0   | 1 |
        | 1 | 0 | 1   | 0 |
        | 1 | 1 | 0   | 1 |
        | 1 | 1 | 1   | 1 |
        """
        not_a: Bit = self.not_gate(a)
        not_b: Bit = self.not_gate(b)
        not_sel: Bit = self.not_gate(sel)

        a0b1sel1: Bit = self.and_gate(self.and_gate(not_a, b), sel)
        a1b0sel0: Bit = self.and_gate(self.and_gate(a, not_b), not_sel)
        a1b1sel0: Bit = self.and_gate(self.and_gate(a, b), not_sel)
        a1b1sel1: Bit = self.and_gate(self.and_gate(a, b), sel)

        return self.or_gate(
            self.or_gate(a0b1sel1, a1b0sel0), self.or_gate(a1b1sel0, a1b1sel1)
        )
