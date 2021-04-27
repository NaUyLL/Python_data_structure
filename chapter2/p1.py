class Rational:
    @staticmethod
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m!=0:
            m, n = n % m, m
        return n

    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)
        self._num = sign * (num // g)
        self._den = den // g


    def num(self):
        return self._num


    def den(self):
        return self._den


    def __add__(self, other):
        den = self._den * other.den()
        num = self._num * other.den() + self._den * other.num()
        return Rational(num, den)


    def __mul__(self, other):
        den = self._den * other.den()
        num = self._num * other.num()
        return Rational(num, den)


    def __eq__(self, other):
        return self._den * other.num() == self._num * other.den()


    def __str__(self):
        return str(self._num) + "/" + str(self._den)


if __name__ == "__main__":
    x = Rational(1, 3)
    y = Rational(2, 3)
    print(x+y)