from bank import value

def test_hello():
    for greeting in ["hello", "Hello", "HELLO", "  hello  ", "  Hello  ", "  HELLO  "]:
        assert value(greeting) == 0

def test_h():
    for greeting in ["hi", "Hi", "HI", "  hi  ", "  Hey  ", "  HI  "]:
        assert value(greeting) == 20

def test_other():
    for greeting in ["what's up?", "good morning!"]:
        assert value(greeting) == 100