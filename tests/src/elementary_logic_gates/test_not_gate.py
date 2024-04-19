from elementary_logic_gates.not_gate import NotGate
from src.types.bits import Bit


def test_not():
    not_gate = NotGate()
    assert not_gate(Bit(0)) == Bit(1)
    assert not_gate(Bit(1)) == Bit(0)
