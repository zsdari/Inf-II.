import unittest
from main import osszead, axb, ax2b

class AdderTest(unittest.TestCase):
    def test_osszead_function(self):
        self.assertEqual(30, osszead(10, 20))

    def test_axb_function(self):
        self.assertEqual(2, axb(2,-4))
        self.assertIsNone(axb(0,-2))

    class TestAx2bFunction(unittest.TestCase):

        def test_ax2b_function(self):
            # Test with a = 0 (linear equation)
            self.assertIsNone(ax2b(0, 0, 5))  # 0x + 0x + 5 = 0 → no solution
            self.assertEqual(ax2b(0, 2, 4), -2)  # 2x + 4 = 0 → x = -2

            # Test with negative determinant (no real roots)
            self.assertIsNone(ax2b(1, 0, 1))  # x² + 1 = 0 → no real roots
            self.assertIsNone(ax2b(2, 1, 3))  # 2x² + x + 3 = 0 → no real roots

            # Test with double root (determinant = 0)
            result = ax2b(1, 2, 1)  # x² + 2x + 1 = 0 → root: -1
            self.assertEqual(result, -1)

            result = ax2b(4, 4, 1)  # 4x² + 4x + 1 = 0 → root: -0.5
            self.assertEqual(result, -0.5)

            # Test with two real roots (determinant > 0)
            result = ax2b(1, -3, 2)  # x² - 3x + 2 = 0 → roots: 2 and 1
            self.assertIsInstance(result, tuple)
            self.assertEqual(len(result), 2)
            x1, x2 = result
            # Order might be different, so check both possibilities
            self.assertTrue((x1 == 2 and x2 == 1) or (x1 == 1 and x2 == 2))

            result = ax2b(1, -5, 6)  # x² - 5x + 6 = 0 → roots: 3 and 2
            self.assertIsInstance(result, tuple)
            x1, x2 = result
            self.assertTrue((x1 == 3 and x2 == 2) or (x1 == 2 and x2 == 3))

    if __name__ == '__main__':
        unittest.main()

if __name__ == '__main__':
    unittest.main()
