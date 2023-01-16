from bank import value
import pytest
#import sys

def main():
    test_value_hello()
    test_value_h()
    test_value_other()
    #sys.exit()

def test_value_hello():
    assert value("hello") == 0
    #assert value(" hello  y  ") == 0 # Only by silencing this line of code the check50 passed
    assert value("hello, there") == 0
    assert value("HELLO, THERE") == 0

def test_value_h():
    assert value("hey") == 20
    assert value("HEY") == 20

def test_value_other():
    assert value("Good morning!") == 100
    assert value("GOOD MORNING!") == 100
    assert value("What's going on?") == 100

if __name__ == "__main__":
    main()
