import Calculator.Items.Item as _item
import Calculator.Operations.Operations as Operations


def setup_chain() -> Operations.Operation:
    add = Operations.Add()
    subtract = Operations.Subtract(add)
    multiply = Operations.Multiply(subtract)
    divide = Operations.Divide(multiply)
    return divide


def main():
    new_item = _item.ItemToWorkWith(first_value=1, second_value=2, operation="+")
    handler_chain = setup_chain()
    print(handler_chain.handle(value=new_item).result)


if __name__ == "__main__":
    main()
