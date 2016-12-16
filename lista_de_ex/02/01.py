import unittest


def igual(a, b):
    if a == b :
        return a
    elif a > b :
        print ('%d na variavel (a) é maior que %d na variavel (b)'%(a, b))
        return a
    else:
        print ('%d na variavel (b) é maior que %d na variavel (a)'%(b, a))
        return b



class NumIgualTestCase(unittest.TestCase):
    def test_igual(self):
        self.assertEqual(1, igual(1,1))
    def test_prim_difernte(self):
        self.assertEqual(2, igual(2,1))
        self.assertEqual(2, igual(1,2))




if __name__ == "__main__":
    unittest.main()
