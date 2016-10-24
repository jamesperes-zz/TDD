import unittest

class Email:

	def __init__(self, email):
		self.email = email

	def extrair_dominio(self):
		return self.email.split('@')[1]


class EmailTestCase(unittest.TestCase):

	def test_extrair_dominio(self):
		email = Email('contato@cursotdd.com.br')
		self.assertEqual(email.extrair_dominio(), 'cursotdd.com.br')

	def test_extrair_dominio_novo_email(self):
		email = Email('foo@bar.com')
		self.assertEqual(email.extrair_dominio(), 'bar.com')
