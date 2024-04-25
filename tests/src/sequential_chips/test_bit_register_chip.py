from src.sequential_chips.bit_register_chip import BitRegisterChip
from src.types.bits import Bit
from pathlib import Path


def test_data_flip_flop_chip():
    bit_register_chip = BitRegisterChip()
    with (Path(__file__).parent / "bit_register_compare.txt").open("r") as file:
        # Skip the first line
        for line in file.read().split("\n")[1:]:
            _, time, in_bit, load, expected_out, _ = line.replace(" ", "").split("|")
            if "+" not in time:
                continue

            in_bit = Bit(in_bit)
            load = Bit(load)
            expected_out = Bit(expected_out)

            print(f"{time} | {in_bit} | {load} | {expected_out}")

            out = bit_register_chip(in_bit, load)

            print(f"{time} | {in_bit} | {load} | {expected_out} | {out}")
