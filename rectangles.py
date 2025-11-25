"""
Zadanie 6.3 z zestawu 6
testy do zadania znajduja sie w pliku test_rectangles.py
"""

from points import Point

class Rectangle:
    """
    Klasa reprezentujaca prostokat na plaszczyznie.
    """

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        """
        Zwraca string w postaci [(x1, y1), (x2, y2)].
        """
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        """
        Zwraca string Rectangle(x1, y1, x2, y2).
        """
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        """
        Zwraca True, jesli oba prostokaty maja identyczne punkty pt1 i pt2.
        """
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        """
        Sprawdza, czy prostokaty są rozne.
        """
        return not self == other

    def center(self):
        """
        Zwraca srodek prostokata jako obiekt Point.
        """
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self):
        """
        Zwraca pole powierzchni prostokata.
        """
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height


    def move(self, x, y):
        """
        Przesuwa prostokat o (x, y).
        """
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self





