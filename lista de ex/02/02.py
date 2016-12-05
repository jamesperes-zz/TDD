import unittest


def soma(a,b,c):
    soma = a + b
    if soma > c :
        print ('soma de %s com %s é maior que %s '%(a,b,c))
    else:
        print('a soma é menor')
    return soma






class somaTestCase(unittest.TestCase):
    def test_somas(self):
        self.assertEqual(2, soma(1,1,1))
        self.assertEqual(2, soma(1,1,5))




if __name__ == "__main__":
    unittest.main()
