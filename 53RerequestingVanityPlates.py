from plates import is_valid

def main():
   test_is_valid_minmaxchar()
   test_is_valid_startletters()
   test_is_valid_nonumbersmiddle()
   test_is_valid_1stnumbernot0()
   test_is_valid_nosymbols()

def test_is_valid_minmaxchar():
    assert is_valid("too long") == False
    assert is_valid("") == False
    assert is_valid("a") == False
    assert is_valid("CS50") == True
    assert is_valid("cs50") == True

def test_is_valid_startletters():
    assert is_valid("ab56") == True
    assert is_valid("AB56") == True
    assert is_valid("a123") == False
    assert is_valid("a12") == False
    assert is_valid("A12") == False

def test_is_valid_nonumbersmiddle():
    assert is_valid("ok333") == True
    assert is_valid("OK333") == True
    assert is_valid("no3a3") == False
    assert is_valid ("no3no") == False

def test_is_valid_1stnumbernot0():
    assert is_valid("ok10") == True
    assert is_valid("no01") == False
    assert is_valid("no0") == False

def test_is_valid_nosymbols():
    assert is_valid("no!12") == False
    assert is_valid("no?12") == False
    assert is_valid("no.12") == False
    assert is_valid("no,12") == False
    assert is_valid("no:12") == False
    assert is_valid("no;12") == False
    assert is_valid("no 12") == False

if __name__ == "__main__":
    main()
