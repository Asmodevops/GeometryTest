import unittest
from geometry.circle import Circle
from geometry.factory import create_shape
from geometry.triangle import Triangle

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), 3.14159, places=4)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=4)

    def test_triangle_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_create_shape_circle(self):
        shape = create_shape(2)
        self.assertAlmostEqual(shape.area(), 12.566, places=3)

    def test_create_shape_triangle(self):
        shape = create_shape(3, 4, 5)
        self.assertAlmostEqual(shape.area(), 6.0, places=3)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

if __name__ == '__main__':
    unittest.main()
