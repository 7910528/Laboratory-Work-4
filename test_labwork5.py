import unittest
from math import pi
from labwork4 import Rectangles, Circle

class TestRectangles(unittest.TestCase):

    def test_valid_rectangle_area(self):
        vertices = [0, 0, 0, 3, 4, 3, 4, 0]
        rect = Rectangles(vertices)
        self.assertAlmostEqual(rect.area(), 12)

    def test_valid_rectangle_perimeter(self):
        vertices = [0, 0, 0, 3, 4, 3, 4, 0]
        rect = Rectangles(vertices)
        self.assertAlmostEqual(rect.perimeter(), 14)

    def test_invalid_rectangle_vertices_length(self):
        vertices = [0, 0, 0, 3, 4, 3]
        with self.assertRaises(ValueError):
            Rectangles(vertices)

    def test_invalid_rectangle_shape(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        with self.assertRaises(ValueError):
            Rectangles(vertices)


class TestCircle(unittest.TestCase):

    def test_valid_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), pi * 25)

    def test_valid_circle_perimeter(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.perimeter(), 2 * pi * 5)

    def test_invalid_circle_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_set_radius(self):
        circle = Circle(5)
        circle.radius = 10
        self.assertAlmostEqual(circle.radius, 10)

    def test_set_invalid_radius(self):
        circle = Circle(5)
        with self.assertRaises(ValueError):
            circle.radius = -10


if __name__ == "__main__":
    unittest.main()
