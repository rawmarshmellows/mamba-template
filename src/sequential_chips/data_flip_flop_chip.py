from src.types.bits import Bit
from typing import Union


class DataFlipFlopChip:
    def __init__(self):
        self.current_return_value = Bit(0)
        self.next_return_value = None
        self.is_first_call = True

    def __call__(self, in_bit: Bit) -> Union[Bit, None]:
        if self.is_first_call:
            self.next_return_value = in_bit
            self.is_first_call = False
            return self.current_return_value

        self.current_return_value = self.next_return_value
        self.next_return_value = in_bit

        return self.current_return_value
