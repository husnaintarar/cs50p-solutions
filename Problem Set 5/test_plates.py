from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start():
    assert is_valid("AB123") == True
    assert is_valid("A123") == False
    assert is_valid("1AB") == False
    assert is_valid("ABCD1") == True

def test_numbers():
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False
    assert is_valid("AB12C") == False
    assert is_valid("AB12!") == False

def test_other():
    assert is_valid("AB") == True