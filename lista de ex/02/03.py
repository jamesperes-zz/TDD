import unittest

def crescente(a,b,c):
    lista = [a,b,c]
    lista.sort()
    return lista







class CrescenteTestCase(unittest.TestCase):
    def test_crescente(self):
        self.assertEqual([1,2,3], crescente(1,2,3))
        self.assertEqual([1,2,3], crescente(3,1,2))



if __name__ == "__main__":
    unittest.main()
