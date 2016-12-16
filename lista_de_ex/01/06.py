import unittest

def soma_fabrica(a):
    fabrica = a + (a*0.45)
    return fabrica

def soma_vendedor(a):
    vendedor = a + (a*0.28)
    return vendedor

def soma_final(a):
    ValorFabrica = a + (a * 0.45)
    ValorVendedor = ValorFabrica + (ValorFabrica * 0.28)
    return ValorVendedor



class ValorFinalTestCase(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(145, soma_fabrica(100))
        self.assertEqual(290, soma_fabrica(200))

    def test_soma_vendedor(self):
        self.assertEqual(128, soma_vendedor(100))

    def test_soma_final(self):
        self.assertEqual(185.6, soma_final(100))

if __name__ == "__main__":
    unittest.main()
