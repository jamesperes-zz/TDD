import unittest

def graus(arg):
    f = (9 * arg + 160) / 5
    return f



class ClimatizadorTestCase(unittest.TestCase):
    def test_graus(self):
        self.assertEqual(50, graus(10))

if __name__ == "__main__":
    unittest.main()
