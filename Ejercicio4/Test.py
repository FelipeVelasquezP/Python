import unittest

from Ejercicio4 import calcularAño


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(2313,calcularAño())
        
if __name__ == '__main__':
    unittest.main()