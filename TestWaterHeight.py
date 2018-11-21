import unittest
from Solution import get_water_height


class TestWaterHeight(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_water_height([3, 2, 1, 2, 3]),
                         [0, 1, 2, 1, 0])
        self.assertEqual(get_water_height([3, 2, 1, 2, 3, 2, 1]),
                         [0, 1, 2, 1, 0, 0, 0])
        self.assertEqual(get_water_height([3, 1, 1, 2, 1, 4]),
                         [0, 2, 2, 1, 2, 0])

    def test_simple_with_zeros(self):
        self.assertEqual(get_water_height([4, 2, 0, 0, 1, 0, 3, 2, 3]),
                         [0, 0, 0, 0, 0, 0, 0, 1, 0])
        self.assertEqual(get_water_height([3, 2, 1, 0, 1, 2, 3]),
                         [0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(get_water_height([3, 1, 0, 3, 1, 4, 1, 2]),
                         [0, 0, 0, 0, 2, 0, 1, 0])
        self.assertEqual(get_water_height([1, 2, 3, 2, 4, 1, 0, 2, 1]),
                         [0, 0, 0, 1, 0, 0, 0, 0, 0])
        self.assertEqual(get_water_height([1, 2, 3, 4, 1, 2, 3, 4, 0, 1, 2, 3, 4]),
                         [0, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0])

    def test_big(self):
        self.assertEqual(get_water_height([12, 1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 9, 0, 1,
                                           2, 4, 6, 7, 8, 9, 1, 2, 4, 5, 2, 1, 10, 1,
                                           2, 4, 5, 6, 7, 9, 1, 6]),
                         [0, 8, 7, 6, 8, 7, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          8, 7, 5, 4, 7, 8, 0, 8, 7, 5, 4, 3, 2, 0, 5, 0])
        self.assertEqual(get_water_height([4, 15, 6, 7, 8, 10, 3, 6, 8, 11, 18, 16, 0,
                                           3, 1, 5, 8, 9, 14, 3, 0, 13, 8, 7, 9, 0, 0,
                                           19, 5, 6, 2, 1, 8, 17]),
                         [0, 0, 9, 8, 7, 5, 12, 9, 7, 4, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,
                          0, 0, 1, 2, 0, 0, 0, 0, 12, 11, 15, 16, 9, 0])


if __name__ == '__main__':
    unittest.main()