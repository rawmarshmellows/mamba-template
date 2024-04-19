from elementary_logic_gates.mux16_gate import Mux16Gate
from src.types.bits import Bits16, Bit


def test_mux16_gate():
    mux16_gate = Mux16Gate()

    # Test case 1: Both inputs are all 0s, sel is 0
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bit(0),
    ) == Bits16.from_string("0000000000000000")

    # Test case 2: Both inputs are all 0s, sel is 1
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0000000000000000"),
        Bit(1),
    ) == Bits16.from_string("0000000000000000")

    # Test case 3: Input b has a specific pattern, sel is 0
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0001001000110100"),
        Bit(0),
    ) == Bits16.from_string("0000000000000000")

    # Test case 4: Input b has a specific pattern, sel is 1
    assert mux16_gate(
        Bits16.from_string("0000000000000000"),
        Bits16.from_string("0001001000110100"),
        Bit(1),
    ) == Bits16.from_string("0001001000110100")

    # Test case 5: Input a has a specific pattern, sel is 0
    assert mux16_gate(
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("0000000000000000"),
        Bit(0),
    ) == Bits16.from_string("1001100001110110")

    # Test case 6: Input a has a specific pattern, sel is 1
    assert mux16_gate(
        Bits16.from_string("1001100001110110"),
        Bits16.from_string("0000000000000000"),
        Bit(1),
    ) == Bits16.from_string("0000000000000000")

    # Test case 7: Alternating patterns for inputs, sel is 0
    assert mux16_gate(
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bit(0),
    ) == Bits16.from_string("1010101010101010")

    # Test case 8: Alternating patterns for inputs, sel is 1
    assert mux16_gate(
        Bits16.from_string("1010101010101010"),
        Bits16.from_string("0101010101010101"),
        Bit(1),
    ) == Bits16.from_string("0101010101010101")
