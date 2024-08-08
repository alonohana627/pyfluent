import unittest
from chapter01.vector import (
    Vector,
)  # assuming Vector class is defined in a module called 'vector'


class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2)
        self.v2 = Vector(3, 4)

    def test_add(self):
        result = self.v1 + self.v2
        self.assertEqual(result, Vector(4, 6))

    def test_mul(self):
        result = self.v1 * 2
        self.assertEqual(result, Vector(2, 4))

    def test_abs(self):
        result = abs(self.v1)
        self.assertEqual(result, 2.23606797749979)


if __name__ == "__main__":
    unittest.main()
