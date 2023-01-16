from fuel import convert, gauge
import pytest

def main():
    test_convert_ValueError()
    test_convert_ZeroDivisionError()
    test_gauge_full()
    test_gauge_empty()
    test_gauge_normal()

def test_convert_ValueError():
    with pytest.raises(ValueError):
        convert("dog")
        convert("dog/cat")
        convert("dog/9")
    with pytest.raises(ValueError):
        convert("-1/4")
        convert("1/-4")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("4/3")


def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_normal():
    assert gauge(75) == "75%"


if __name__ == "__main__":
    main()
