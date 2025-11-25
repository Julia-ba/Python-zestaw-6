import unittest
from points import Point

class TestPoints(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(-3, 4)
        self.p3 = Point(1, 2)

    def test_str_and_repr(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(repr(self.p1), "Point(1, 2)")

    def test_equality(self):
        self.assertTrue(self.p1 == self.p3)
        self.assertFalse(self.p1 == self.p2)
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p1 != self.p3)

    def test_addition(self):
        result = self.p1 + self.p2
        self.assertEqual(result, Point(-2, 6))

    def test_subtraction(self):
        result = self.p1 - self.p2
        self.assertEqual(result, Point(4, -2))

    def test_scalar_multiplication(self):
        result = self.p1 * self.p2
        self.assertEqual(result, 5)

    def test_cross_product(self):
        result = self.p1.cross(self.p2)
        self.assertEqual(result, 10)

    def test_length(self):
        self.assertAlmostEqual(Point(-3, 4).length(), 5.0)

    def test_hash(self):
        s = {Point(1, 2), Point(1, 2), Point(-3, 4)}
        self.assertEqual(len(s), 2)

if __name__ == "__main__":
    unittest.main()



