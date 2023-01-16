from um import count
import pytest

def main():
    test_count()

def test_count():
    assert count("Um") == 1
    assert count("I don't, um, know..") == 1
    assert count("yummy") == 0
    assert count("umbrella") == 0

if __name__ == "__main__":
    main()
