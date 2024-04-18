from elementary_logic_gates.dmux_gate import DmuxGate


def test_dmux_gate():
    dmux_gate = DmuxGate()
    assert dmux_gate(0, 0) == (0, 0)
    assert dmux_gate(0, 1) == (0, 0)
    assert dmux_gate(1, 0) == (1, 0)
    assert dmux_gate(1, 1) == (0, 1)
