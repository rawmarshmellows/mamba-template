from elementary_logic_gates.dmux_gate import DmuxGate
from src.types.bits import Bit


def test_dmux_gate():
    dmux_gate = DmuxGate()
    assert dmux_gate(Bit(0), Bit(0)) == (Bit(0), Bit(0))
    assert dmux_gate(Bit(0), Bit(1)) == (Bit(0), Bit(0))
    assert dmux_gate(Bit(1), Bit(0)) == (Bit(1), Bit(0))
    assert dmux_gate(Bit(1), Bit(1)) == (Bit(0), Bit(1))
