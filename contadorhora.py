import unittest
print ("\n contador de horas!\n\n ")

recebe_tipo = input("digite se for mes ou dia: ")
recebe_num = int(input('Digite o numero: '))

def tipo(n):
    if n == 'mes':
        return mes_dia
    else:
        return dia_hora



def mes_dia(n):
    resul=(n * 30)
    return resul

def dia_hora(n):
    resul=(n * 24)
    return resul

class ContadorTestCase(unittest.TestCase):
    def teste_mes_dia(self):
        self.assertEqual(30, mes_dia(1))
        self.assertEqual(60, mes_dia(2))

    def teste_dia_hora(self):
        self.assertEqual(24, dia_hora(1))
        self.assertEqual(48, dia_hora(2))

    def teste_tipo(self):
        self.assertEqual(mes_dia,tipo('mes'))
        self.assertEqual(dia_hora,tipo('dia'))


if __name__ == "__main__":
    unittest.main()
