from working import convert
import pytest

def main():
    test_convert_wrong_timehourmin()
    test_convert_wrong_match()
    test_get_24h_format_supershort()

def test_convert_wrong_timehourmin():
    with pytest.raises(ValueError):
        convert("13 PM to 14 AM")
    with pytest.raises(ValueError):
        convert("9:62 AM to 5:74 PM")
    with pytest.raises(ValueError):
        convert("13:62 PM to 14:74 AM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")

def test_convert_wrong_match():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("cat")

def test_get_24h_format_supershort():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

if __name__ == "__main__":
    main()
