import unittest
print ("\n nascido por hora!\n\n ")


def nascido_dia(n):
    resul=int((n/12)/30)
    return resul


class nascidoTestCase(unittest.TestCase):
    def teste_resultado(self):
        self.assertEqual(1, nascido_dia(500))



if __name__ == "__main__":
    unittest.main()
