import unittest

def ar (arg1, arg2):
    area = (arg1 * arg2) / 2
    return area


class AreaTestCase(unittest.TestCase):
    def test_ar(self):
        self.assertEqual(2, ar(2,2))

if __name__ == "__main__":
    unittest.main()
