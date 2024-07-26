import unittest
from calc import sum

class TestCalc(unittest.TestCase):
    
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(sum(-5, 5), 0)        

unittest.main(verbosity=2)
