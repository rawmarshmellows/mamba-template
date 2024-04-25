from src.types.bits import Bit
from src.elementary_logic_gates.mux_gate import MuxGate
from .data_flip_flop_chip import DataFlipFlopChip


class BitRegisterChip:
    def __init__(self):
        self.data_flip_flop_chip = DataFlipFlopChip()
        self.mux_gate = MuxGate()

    def __call__(self, in_bit: Bit, load: Bit) -> Bit:
        previous_data_flip_flop_chip_value = self.data_flip_flop_chip(in_bit)
        mux_output = self.mux_gate(previous_data_flip_flop_chip_value, in_bit, load)
        return self.data_flip_flop_chip(mux_output)
