class Jar:
    def __init__(self, capacity=12):
        # capacity if the max number of cookies that can fit in the jar
        # if capacity is negative int, raise ValueError
        if capacity < 0 and capacity.is_integer() == False:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # return a str with n 🍪, n = the number of cookies in the cookie jar
        # return f"In the cooky jar there are {n} cookies"
        return self._size * "🍪"

    def deposit(self, n):
        # add n cookies to the jar
        # if by adding n in the jar, the total cookies > capacity raise a ValueError

        if (self.size + n) > self.capacity:
            raise ValueError("Not enough capacity")
        else:
            self._size = self._size + n

    def withdraw(self, n):
        # withdraw n cookies from the jar
        # if the capacity is < wanted n cookies, raise ValueError

        if self.size < n:
            raise ValueError("Not enough cookies")
        else:
            self._size = self._size - n

    @property
    def capacity(self):
        # return the capacity of the cookie jar
        return self._capacity

    @property
    def size(self):
        # return the number of cookies currently in the jar
        return self._size


def main():
    jar = Jar()
    n_added = int(input("Cookies to add to the jar: "))
    n_withdrawn = int(input("Cookies to withdraw from the jar: "))
    jar.deposit(n = n_added)
    jar.withdraw(n = n_withdrawn)
    print(jar)


if __name__ == "__main__":
    main()

"""
jar = Jar()
jar.deposit(3)
print(jar)
jar.withdraw(1)
print(jar)
"""
