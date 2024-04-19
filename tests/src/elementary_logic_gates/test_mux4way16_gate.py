# from elementary_logic_gates.mux4way16_gate import Mux4Way16Gate
# from src.types.bits import Bits16, Bits2


# def test_mux4way16_gate():
#     mux4way16_gate = Mux4Way16Gate()

#     # Test cases where all inputs are zeros
#     assert mux4way16_gate(
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits2.from_string("00"),
#     ) == Bits16.from_string("0000000000000000")

#     assert mux4way16_gate(
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits2.from_string("01"),
#     ) == Bits16.from_string("0000000000000000")

#     assert mux4way16_gate(
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits2.from_string("10"),
#     ) == Bits16.from_string("0000000000000000")

#     assert mux4way16_gate(
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits16.from_string("0000000000000000"),
#         Bits2.from_string("11"),
#     ) == Bits16.from_string("0000000000000000")

#     # Test cases with specific inputs and selection
#     assert mux4way16_gate(
#         Bits16.from_string("0001001000110100"),
#         Bits16.from_string("1001100001110110"),
#         Bits16.from_string("1010101010101010"),
#         Bits16.from_string("0101010101010101"),
#         Bits2.from_string("00"),
#     ) == Bits16.from_string("0001001000110100")

#     assert mux4way16_gate(
#         Bits16.from_string("0001001000110100"),
#         Bits16.from_string("1001100001110110"),
#         Bits16.from_string("1010101010101010"),
#         Bits16.from_string("0101010101010101"),
#         Bits2.from_string("01"),
#     ) == Bits16.from_string("1001100001110110")

#     assert mux4way16_gate(
#         Bits16.from_string("0001001000110100"),
#         Bits16.from_string("1001100001110110"),
#         Bits16.from_string("1010101010101010"),
#         Bits16.from_string("0101010101010101"),
#         Bits2.from_string("10"),
#     ) == Bits16.from_string("1010101010101010")

#     assert mux4way16_gate(
#         Bits16.from_string("0001001000110100"),
#         Bits16.from_string("1001100001110110"),
#         Bits16.from_string("1010101010101010"),
#         Bits16.from_string("0101010101010101"),
#         Bits2.from_string("11"),
#     ) == Bits16.from_string("0101010101010101")
