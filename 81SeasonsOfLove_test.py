from seasons import format_date
import pytest

def main():
    test_format_date()


def test_format_date():
    assert format_date("1993-01-15") == "1993-01-15"
    assert format_date("Januray 1st 1993") == None


if __name__ == "__main__":
    main()
