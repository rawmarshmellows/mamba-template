from elementary_logic_gates.nand_gate import NandGate


def test_nand_gate():
    nand_gate = NandGate()
    assert nand_gate(0, 0) == 1
    assert nand_gate(0, 1) == 1
    assert nand_gate(1, 0) == 1
    assert nand_gate(1, 1) == 0
