import unittest
import mymodule
class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        edadFutura = calcularEdadFutura(19,2020)
        self.assertEqual(mymodule.sum(5, 7), 12)
    