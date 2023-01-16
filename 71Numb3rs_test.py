from numb3rs import validate
import pytest

def main():
    test_validate_dots()
    test_validate_nondigits()
    test_validate_rangesdigits()
    test_validate_nrspots()

def test_validate_dots():
    assert validate("4,56,74,4") == False
    assert validate("4,56.74.4") == False
    assert validate("4;56.74-4") == False
    assert validate("1.2.3.4.") == False
    assert validate(".1.2.3.4") == False
    assert validate(".1.2.3.4.") == False
    assert validate("23.12.125.99") == True

def test_validate_nondigits():
    assert validate("dog") == False
    assert validate("dog.cat.horse.donkey") == False
    assert validate("dog.cat.1.2") == False
    assert validate("1.cat.1.2") == False

def test_validate_rangesdigits():
    assert validate("1.2.3.1000") == False
    assert validate("1.2.1000.4") == False
    assert validate("1.1000.3.4") == False
    assert validate("1000.2.3.4") == False
    assert validate("256.256.256.256") == False
    assert validate("1.2.3.4") == True
    assert validate("75.456.76.65") == False

def test_validate_nrspots():
    assert validate("1.2.3.4.5") == False
    assert validate("1.") == False
    assert validate("1.2.") == False
    assert validate("1.2.3.") == False
    assert validate("44.54.12.21") == True

if __name__ == "__main__":
    main()
