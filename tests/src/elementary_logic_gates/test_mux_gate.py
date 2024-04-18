from elementary_logic_gates.mux_gate import MuxGate


def test_mux_gate():
    mux_gate = MuxGate()
    assert mux_gate(0, 0, 0) == 0
    assert mux_gate(0, 0, 1) == 0
    assert mux_gate(0, 1, 0) == 0
    assert mux_gate(0, 1, 1) == 1
    assert mux_gate(1, 0, 0) == 1
    assert mux_gate(1, 0, 1) == 0
    assert mux_gate(1, 1, 0) == 1
    assert mux_gate(1, 1, 1) == 1
