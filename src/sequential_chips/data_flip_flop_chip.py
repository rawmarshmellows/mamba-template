from src.types.bits import Bit


class DataFlipFlopChipPerformance:
    def __init__(self):
        self.current_return_value = 0
        self.next_return_value = None
        self.is_first_call = True

    def __call__(self, in_bit: int) -> int:
        if self.is_first_call:
            self.next_return_value = in_bit
            self.is_first_call = False
            return self.current_return_value

        self.current_return_value = self.next_return_value
        self.next_return_value = in_bit

        return self.current_return_value


class DataFlipFlopChip:
    def __init__(self):
        self.current_return_value = Bit(0)
        self.next_return_value = None
        self.is_first_call = True

    def __call__(self, in_bit: Bit) -> Bit:
        if self.is_first_call:
            self.next_return_value = in_bit
            self.is_first_call = False
            return self.current_return_value

        self.current_return_value = self.next_return_value
        self.next_return_value = in_bit

        return self.current_return_value
