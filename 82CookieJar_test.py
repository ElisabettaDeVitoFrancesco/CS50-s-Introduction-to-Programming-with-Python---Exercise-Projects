from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(7)
    assert jar.size == 11


def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
