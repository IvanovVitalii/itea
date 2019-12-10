# OOP


class Point:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y, self._z + other._z)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y, self._z - other._z)

    def __mul__(self, other):
        return Point(self._x * other._x, self._y * other._y, self._z * other._z)

    def __truediv__(self, other):
        return Point(self._x / other._x, self._y / other._y, self._z / other._z)

    def get_point(self):
        return self._x, self._y, self._z

    def get_x(self, x):
        return  self._x

    def get_y(self, y):
        return  self._y

    def get_z(self, z):
        return  self._z

    def set_point(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z


point1 = Point(1, 2, 3)
point2 = Point(1, 2, 3)
print(point1.get_point())
mul_points = point1 * point2
print(mul_points.get_point())
point1.set_point(2, 2, 4)
print((point2 - point1).get_point())
print(mul_points)
point1.set_x(10)
print(point1.get_x(10))
print(point1.get_point())

