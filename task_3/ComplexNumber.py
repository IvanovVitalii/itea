class ComplexNumber:

    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b
        self._complex_number = ''

    def __add__(self, other):
        return ComplexNumber(self._a + other._a, self._b + other._b)

    def __sub__(self, other):
        return ComplexNumber(self._a - other._a, self._b - other._b)

    def __mul__(self, other):
        return ComplexNumber((self._a * other._a - self._b * other._b), (self._a * other._b + self._b * other._a))

    def __truediv__(self, other):
        return ComplexNumber((self._a * other._a + self._b * other._b)/(other._a * other._a + other._b * other._b),
                             (self._b * other._a - self._a * other._b)/(other._a * other._a + other._b * other._b))

    def set_complex_number(self, a, b):
        self._a = a
        self._b = b

    def get_complex_number(self):
        if self._a % 1 == 0:
            self._a = int(self._a)
        if self._b % 1 == 0:
            self._b = int(self._b)
        if self._a != 0 and self._b == 0:
            c_n = self._complex_number = f'{self._a}'
        elif self._a != 0 and self._b < 0:
            c_n = self._complex_number = f'{self._a}{self._b}i'
        elif self._a != 0 and self._b > 0:
            c_n = self._complex_number = f'{self._a}+{self._b}i'
        elif self._a == 0 and self._b != 0:
            c_n = self._complex_number = f'{self._b}i'
        return c_n


complex_number1 = ComplexNumber()
complex_number1.set_complex_number(2, 5)
print(complex_number1.get_complex_number())
complex_number2 = ComplexNumber()
complex_number2.set_complex_number(5, -2)

add_complex_number = complex_number1 + complex_number2
sub_complex_number = complex_number1 - complex_number2
mul_complex_number = complex_number1 * complex_number2
truediv_complex_number = complex_number1 / complex_number2

print(add_complex_number.get_complex_number())
print(sub_complex_number.get_complex_number())
print(mul_complex_number.get_complex_number())
print(truediv_complex_number.get_complex_number())