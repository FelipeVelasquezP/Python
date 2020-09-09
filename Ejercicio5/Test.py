import unittest

from Ejercicio5 import calcularSerie


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual("122333444455555",calcularSerie(5))
        
if __name__ == '__main__':
    unittest.main()