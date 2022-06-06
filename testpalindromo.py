import unittest
from palindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    __palindromo = None

    def setUp(self):
        self.__palindromo = Palindromo('neuquen')

    def testUnPalindromoPar(self):
        self.assertEqual(self.__palindromo.esPalindromo(), True)

    def testNoPalindromo(self):
        self.__palindromo.setPalabra('polinomio')
        self.assertEqual(self.__palindromo.esPalindromo(), False)


if __name__ == '__main__':
    unittest.main()
