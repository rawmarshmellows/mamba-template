from elementary_logic_gates.not16_gate import Not16Gate
from src.types.bits import Bits16


def test_not16_gate():
    not16_gate = Not16Gate()

    # Test case 1: All 0s input
    assert not16_gate(Bits16.from_string("0000000000000000")) == Bits16.from_string(
        "1111111111111111"
    )

    # Test case 2: All 1s input
    assert not16_gate(Bits16.from_string("1111111111111111")) == Bits16.from_string(
        "0000000000000000"
    )

    # Test case 3: Alternating 1s and 0s starting with 1
    assert not16_gate(Bits16.from_string("1010101010101010")) == Bits16.from_string(
        "0101010101010101"
    )

    # Test case 4: Specific pattern
    assert not16_gate(Bits16.from_string("0011110011000011")) == Bits16.from_string(
        "1100001100111100"
    )

    # Test case 5: Another specific pattern
    assert not16_gate(Bits16.from_string("0001001000110100")) == Bits16.from_string(
        "1110110111001011"
    )
