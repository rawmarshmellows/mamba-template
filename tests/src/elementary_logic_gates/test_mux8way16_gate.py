from elementary_logic_gates.mux8way16_gate import Mux8Way16Gate
from src.types.bits import Bits16, Bits3


def test_mux8way16_gate():
    mux8way16_gate = Mux8Way16Gate()

    # Test where all inputs are zero
    zero = Bits16.from_string("0000000000000000")
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("000")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("001")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("010")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("011")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("100")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("101")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("110")
        )
        == zero
    )
    assert (
        mux8way16_gate(
            zero, zero, zero, zero, zero, zero, zero, zero, Bits3.from_string("111")
        )
        == zero
    )

    # Test with specific non-zero values
    a = Bits16.from_string("0001001000110100")
    b = Bits16.from_string("0010001101000101")
    c = Bits16.from_string("0011010001010110")
    d = Bits16.from_string("0100010101100111")
    e = Bits16.from_string("0101011001111000")
    f = Bits16.from_string("0110011110001001")
    g = Bits16.from_string("0111100010011010")
    h = Bits16.from_string("1000100110101011")

    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("000")) == a
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("001")) == b
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("010")) == c
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("011")) == d
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("100")) == e
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("101")) == f
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("110")) == g
    assert mux8way16_gate(a, b, c, d, e, f, g, h, Bits3.from_string("111")) == h
