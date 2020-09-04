import unittest

from Ejercicio2 import validarNumero


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(False,validarNumero(int(9)))
        self.assertEqual(True,validarNumero(int(892)))
        
if __name__ == '__main__':
    unittest.main()