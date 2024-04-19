from elementary_logic_gates.nand_gate import NandGate
from src.types.bits import Bit


def test_nand_gate():
    nand_gate = NandGate()
    assert nand_gate(Bit(0), Bit(0)) == Bit(1)
    assert nand_gate(Bit(0), Bit(1)) == Bit(1)
    assert nand_gate(Bit(1), Bit(0)) == Bit(1)
    assert nand_gate(Bit(1), Bit(1)) == Bit(0)
