from src.types.bits import Bit


class DataFlipFlopChipPerformance:
    def __init__(self):
        self.current_value = 0
        self.next_value = None
        self.is_first_call = True

    def __call__(self, in_bit: int) -> int:
        if self.is_first_call:
            self.next_value = in_bit
            self.is_first_call = False
            return self.current_value

        self.current_value = self.next_value
        self.next_value = in_bit

        return self.current_value


class DataFlipFlopChip:
    def __init__(self):
        self.current_value = Bit(0)
        self.next_value = None
        self.is_first_call = True

    def __call__(self, in_bit: Bit) -> Bit:
        if self.is_first_call:
            self.next_value = in_bit
            self.is_first_call = False
            return self.current_value

        self.current_value = self.next_value
        self.next_value = in_bit

        return self.current_value
