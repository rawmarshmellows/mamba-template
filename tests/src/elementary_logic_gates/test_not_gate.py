from elementary_logic_gates.not_gate import NotGate


def test_not():
    not_gate = NotGate()
    assert not_gate(0) == 1
    assert not_gate(1) == 0
