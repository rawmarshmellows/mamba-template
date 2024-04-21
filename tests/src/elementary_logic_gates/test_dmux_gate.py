from elementary_logic_gates.dmux_gate import DmuxGate
from src.types.bits import Bit, Bits2


def test_dmux_gate():
    dmux_gate = DmuxGate()
    assert dmux_gate(Bit(0), Bit(0)) == Bits2.from_string("00")
    assert dmux_gate(Bit(0), Bit(1)) == Bits2.from_string("00")
    assert dmux_gate(Bit(1), Bit(0)) == Bits2.from_string("10")
    assert dmux_gate(Bit(1), Bit(1)) == Bits2.from_string("01")
