import unittest

from Ejercicio1 import calcularEdadFutura


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(69,calcularEdadFutura(2020,19))
        
if __name__ == '__main__':
    unittest.main()