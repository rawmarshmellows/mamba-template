from combinational_chips.inc16_chip import Inc16Chip
from src.types.bits import Bits16


def test_inc16_chip():
    inc16_chip = Inc16Chip()

    assert inc16_chip(Bits16.from_string("0000000000000000")) == Bits16.from_string(
        "0000000000000001"
    ), "Failed for input 0000000000000000"
    assert inc16_chip(Bits16.from_string("1111111111111111")) == Bits16.from_string(
        "0000000000000000"
    ), "Failed for input 1111111111111111"
    assert inc16_chip(Bits16.from_string("0000000000000101")) == Bits16.from_string(
        "0000000000000110"
    ), "Failed for input 0000000000000101"
    assert inc16_chip(Bits16.from_string("1111111111111011")) == Bits16.from_string(
        "1111111111111100"
    ), "Failed for input 1111111111111011"


# Example usage of the test function
if __name__ == "__main__":
    test_inc16_chip()
