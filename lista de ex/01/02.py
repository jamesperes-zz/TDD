#lata tem 2l e gasta 3l por metro

import unittest


def area(a, b):
    rarea = (a * b)
    return rarea

def gasto(a):
    rgasto = (a / 3)
    return rgasto

def numlat(a, b):
    rnumlat = ()



class PinturaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(4, area(2,2))

    def test_gasto(self):
        self.assertEqual(2, gasto(6))

    def test_numlat(self):
        self.assertEqual(8, numlat(4))

if __name__ == "__main__":
    unittest.main()
