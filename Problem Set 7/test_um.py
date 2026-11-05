from um import count

def test_case():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1

def test_word_with_punctuation():
    assert count("um?") == 1
    assert count("um, hello, um, world") == 2
    assert count("Hello, um!") == 1

def test_substring():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("circumstance") == 0
    assert count("Um, thanks for the album.") == 1