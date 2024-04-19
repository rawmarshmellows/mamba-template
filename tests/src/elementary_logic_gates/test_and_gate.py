from elementary_logic_gates.and_gate import AndGate
from src.types.bits import Bit


def test_and_gate():
    and_gate = AndGate()
    assert and_gate(Bit(0), Bit(0)) == Bit(0)
    assert and_gate(Bit(0), Bit(1)) == Bit(0)
    assert and_gate(Bit(1), Bit(0)) == Bit(0)
    assert and_gate(Bit(1), Bit(1)) == Bit(1)
