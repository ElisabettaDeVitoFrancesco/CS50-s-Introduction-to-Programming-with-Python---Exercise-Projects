from twttr import shorten
import pytest

def main():
    test_shorten_low()
    test_shorten_cap()
    test_shorten_number()
    test_shorten_punct()

def test_shorten_low():
    assert shorten("hello") == "hll"

def test_shorten_cap():
    assert shorten("hEllO") == "hll"

def test_shorten_number():
    assert shorten("CS50") == "CS50"

def test_shorten_punct():
    assert shorten("What's up?") == "Wht's p?"

if __name__ == "__main__":
    main()
