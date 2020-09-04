import unittest

from Ejercicio3 import calcularDescuento


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(9000,calcularDescuento(900000,"j"))
        
if __name__ == '__main__':
    unittest.main()