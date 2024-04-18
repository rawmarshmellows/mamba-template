from elementary_logic_gates.xor_gate import XorGate


def test_xor_gate():
    xor_gate: XorGate = XorGate()
    assert xor_gate(0, 0) == 0
    assert xor_gate(0, 1) == 1
    assert xor_gate(1, 0) == 1
    assert xor_gate(1, 1) == 0
