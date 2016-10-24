import unittest

class Email:

	def __init__(self, email):
		pass

	def extrair_dominio(self):
		pass




class EmailTestCase(unittest.TestCase):

	def test_extrair_dominio(self):
		email = Email('contato@cursotdd.com.br')
		self.assertEqual(email.extrair_dominio(), 'cursotdd.com.br')
