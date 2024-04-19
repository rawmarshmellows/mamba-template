from elementary_logic_gates.or_gate import OrGate
from src.types.bits import Bit


def test_or_gate():
    or_gate = OrGate()
    assert or_gate(Bit(0), Bit(0)) == Bit(0)
    assert or_gate(Bit(0), Bit(1)) == Bit(1)
    assert or_gate(Bit(1), Bit(0)) == Bit(1)
    assert or_gate(Bit(1), Bit(1)) == Bit(1)
