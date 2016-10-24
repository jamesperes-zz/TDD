import unittest

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n

def listar_fizzbuzz(n):
    i=1
    li = []
    while i <= n:
        li.append(fizzbuzz(i))
        i+=1
    return li


class FizzBuzzTestCase(unittest.TestCase):

    def test_fizzbuzz_deve_retornar_numero(self):
        self.assertEqual(1, fizzbuzz(1))
        self.assertEqual(2, fizzbuzz(2))

    def test_fizzbuzz_deve_retornar_fizz(self):
        self.assertEqual('fizz', fizzbuzz(3))
        self.assertEqual('fizz', fizzbuzz(6))

    def test_fizzbuzz_deve_retornar_buzz(self):
        self.assertEqual('buzz', fizzbuzz(5))

    def test_fizzbuzz_deve_retornar_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizzbuzz(15))

    def test_listar_fizzbuzz(self):
        esperado = [1, 2, 'fizz', 4, 'buzz']
        self.assertEqual(esperado, listar_fizzbuzz(n=5))


if __name__ == "__main__":
    unittest.main()
