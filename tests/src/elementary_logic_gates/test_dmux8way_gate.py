from elementary_logic_gates.dmux8way_gate import Dmux8WayGate
from src.types.bits import Bit, Bits3, Bits8


def test_dmux8way_gate():
    dmux8way_gate = Dmux8WayGate()

    # Test cases where the input is 0
    assert dmux8way_gate(Bit(0), Bits3.from_string("000")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("001")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("010")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("011")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("100")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("101")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("110")) == Bits8.from_string(
        "00000000"
    )
    assert dmux8way_gate(Bit(0), Bits3.from_string("111")) == Bits8.from_string(
        "00000000"
    )

    # Test cases where the input is 1
    assert dmux8way_gate(Bit(1), Bits3.from_string("000")) == Bits8.from_string(
        "10000000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("001")) == Bits8.from_string(
        "01000000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("010")) == Bits8.from_string(
        "00100000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("011")) == Bits8.from_string(
        "00010000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("100")) == Bits8.from_string(
        "00001000"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("101")) == Bits8.from_string(
        "00000100"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("110")) == Bits8.from_string(
        "00000010"
    )
    assert dmux8way_gate(Bit(1), Bits3.from_string("111")) == Bits8.from_string(
        "00000001"
    )


# Example usage of the test function
if __name__ == "__main__":
    test_dmux8way_gate()
