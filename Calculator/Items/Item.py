from dataclasses import dataclass


@dataclass
class ItemToWorkWith:
    def __init__(self, first_value, second_value, operation):
        self.first_value = first_value
        self.second_value = second_value
        self.operation = operation

    first_value: float
    second_value: float
    operation: str
    result: float
