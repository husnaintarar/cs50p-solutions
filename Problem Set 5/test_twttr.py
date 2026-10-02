from twttr import shorten

def test_shorten():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("Python") == "Pythn"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("This is a test.") == "Ths s  tst."
    assert shorten("CS50P") == "CS50P"

