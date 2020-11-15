from Memento.graphics import *


class Memento_object(object):
    _saved_text = ""

    def __init__(self, text):
        self._saved_text = text

    def get_saved_text(self) -> str:
        return self._saved_text


class CareTaker(object):
    saved_texts = []

    def add_memento(self, memento: Memento_object):
        self.saved_texts.append(memento)

    def get_memento(self, index):
        return self.saved_texts[index]


class Originator(Text):
    def __init__(self, text, p):
        super().__init__(p, text)

    def get_from_memento(self, Memento):
        print("getting from memento")
        self.setText(text=Memento.get_saved_text())

    def send_to_memento(self):
        print("saving to memento")
        return Memento_object(text=self.getText())


class CareTakerWrapper:
    # for multiple objects, to associate the caretaker w/ its originator
    def __init__(self, some_caretaker, some_originator):
        self.caretaker = some_caretaker
        self.originator = some_originator

    def new_text_and_save(self, new_text: str):
        self.originator.setText(text=new_text)
        self.caretaker.add_memento(self.originator.send_to_memento())


def main():

    temp_caretaker = CareTaker()
    some_text = Originator(p=Point(200, 200), text="Hello world")
    temp_caretaker.add_memento(some_text.send_to_memento())
    some_wrapper = CareTakerWrapper(temp_caretaker, some_text)
    some_wrapper.new_text_and_save(new_text="hello world 1")
    some_wrapper.new_text_and_save(new_text="hello world 2")
    some_wrapper.new_text_and_save(new_text="hello world 3")
    some_wrapper.new_text_and_save(
        new_text="Use left and right keys to cycle through states"
    )
    win = GraphWin(width=500, height=500)
    some_wrapper.originator.draw(win)
    index = len(some_wrapper.caretaker.saved_texts) - 1
    print(len(some_wrapper.caretaker.saved_texts))
    print(index)
    while index > 0:
        keypress = win.getKey()
        if keypress == "Left":
            index = index - 1
        elif keypress == "Right":
            index = min(index + 1, len(some_wrapper.caretaker.saved_texts) - 1)

        some_wrapper.originator.get_from_memento(
            some_wrapper.caretaker.get_memento(index=index)
        )
    exit=Text(Point(100,100),text="Click to exit")
    exit.draw(graphwin=win)
    win.getMouse()
    win.close()


main()
