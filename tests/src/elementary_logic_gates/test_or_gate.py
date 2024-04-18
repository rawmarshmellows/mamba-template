from elementary_logic_gates.or_gate import OrGate


def test_or_gate():
    or_gate = OrGate()
    assert or_gate(0, 0) == 0
    assert or_gate(0, 1) == 1
    assert or_gate(1, 0) == 1
    assert or_gate(1, 1) == 1
