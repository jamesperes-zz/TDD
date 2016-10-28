import unittest

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))


def soma(a, b):
    rsoma = (a + b)
    return rsoma

def produto(a, b):
    rproduto = (a * b)
    return rproduto



print (n1, n2, soma(n1,n2), produto(n1,n2))

class ContaTestCase(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(20, soma(10,10))

    def test_produto(self):
        self.assertEqual(100, produto(10,10))

if __name__ == "__main__":
    unittest.main()
