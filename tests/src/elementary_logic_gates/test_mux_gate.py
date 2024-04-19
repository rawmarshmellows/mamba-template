from elementary_logic_gates.mux_gate import MuxGate
from src.types.bits import Bit


def test_mux_gate():
    mux_gate = MuxGate()
    assert mux_gate(Bit(0), Bit(0), Bit(0)) == Bit(0)
    assert mux_gate(Bit(0), Bit(0), Bit(1)) == Bit(0)
    assert mux_gate(Bit(0), Bit(1), Bit(0)) == Bit(0)
    assert mux_gate(Bit(0), Bit(1), Bit(1)) == Bit(1)
    assert mux_gate(Bit(1), Bit(0), Bit(0)) == Bit(1)
    assert mux_gate(Bit(1), Bit(0), Bit(1)) == Bit(0)
    assert mux_gate(Bit(1), Bit(1), Bit(0)) == Bit(1)
    assert mux_gate(Bit(1), Bit(1), Bit(1)) == Bit(1)
