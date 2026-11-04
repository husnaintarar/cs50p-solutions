from numb3rs import validate

def test_format():
    # Test text inputs, and IPs with too few or too many segments
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2..4") == False

def test_range():
    # Test values over 255 across different bytes (especially the first and last)
    assert validate("256.1.1.1") == False
    assert validate("1.300.1.1") == False
    assert validate("1.1.500.1") == False
    assert validate("1.1.1.256") == False
    assert validate("999.999.999.999") == False

def test_valid():
    # Test valid boundary limits and normal IPs
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("192.168.1.1") == True

