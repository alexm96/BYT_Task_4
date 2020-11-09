from __future__ import annotations
from abc import abstractmethod
from Calculator.Items.Item import ItemToWorkWith


class Operation(object):
    def __init__(self, next_in_chain: Operation = None):
        self.next_in_chain = next_in_chain

    @abstractmethod
    def handle(self, value: ItemToWorkWith) -> ItemToWorkWith:
        print("Exists only to be overridden")
        return None


class Subtract(Operation):
    def handle(self, value: ItemToWorkWith) -> ItemToWorkWith:
        if value.operation == "-":
            value.result = value.first_value - value.second_value
            return value
        elif self.next_in_chain is not None:
            return self.next_in_chain.handle(value=value)
        else:
            value.result = None  # end of chain without meeting value
            return value


class Divide(Operation):
    def handle(self, value: ItemToWorkWith) -> ItemToWorkWith:
        if value.operation == "/":
            value.result = value.first_value / value.second_value
            return value
        elif self.next_in_chain is not None:
            return self.next_in_chain.handle(value=value)
        else:
            value.result = None  # end of chain without meeting value
            return value


class Add(Operation):
    def handle(self, value: ItemToWorkWith) -> ItemToWorkWith:
        if value.operation == "+":
            value.result = value.first_value + value.second_value
            return value
        elif self.next_in_chain is not None:
            return self.next_in_chain.handle(value=value)
        else:
            value.result = None  # end of chain without meeting value
            return value


class Multiply(Operation):
    def handle(self, value: ItemToWorkWith) -> ItemToWorkWith:
        if value.operation == "*":
            value.result = value.first_value * value.second_value
            return value
        elif self.next_in_chain is not None:
            return self.next_in_chain.handle(value=value)
        else:
            value.result = None  # end of chain without meeting value
            return value
