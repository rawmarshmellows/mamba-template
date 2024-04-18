from elementary_logic_gates.and_gate import AndGate


def test_and_gate():
    and_gate = AndGate()
    assert and_gate(0, 0) == 0
    assert and_gate(0, 1) == 0
    assert and_gate(1, 0) == 0
    assert and_gate(1, 1) == 1
