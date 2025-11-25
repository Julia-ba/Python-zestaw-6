import unittest
from rectangles import Rectangle
from points import Point

class TestRectangles(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(0,1, 4, 5)
        self.r2 = Rectangle(1,2, 3, 4)

    def test_str_and_repr(self):
        self.assertEqual(str(self.r1), "[(0, 1), (4, 5)]")
        self.assertEqual(repr(self.r1), "Rectangle(0, 1, 4, 5)")

    def test_equality(self):
        self.assertTrue(Rectangle(0, 1, 4, 5) == Rectangle(0, 1, 4, 5))
        self.assertFalse(Rectangle(0, 1, 4, 5) == Rectangle(1, 1, 5, 4))
        self.assertTrue(Rectangle(0, 1, 4, 5) != Rectangle(1, 0, 5, 4))

    def test_center(self):
         c = self.r1.center()
         self.assertEqual(c, Point(2, 3))

    def test_area(self):
        self.assertEqual(self.r1.area(), 16)
        self.assertEqual(self.r2.area(), 4)

    def test_move(self):
        r = Rectangle(0, 0, 4, 4)
        r.move(3, 4)
        self.assertEqual(r.pt1, Point(3, 4))
        self.assertEqual(r.pt2, Point(7, 8))

if __name__ == "__main__":
    unittest.main()

