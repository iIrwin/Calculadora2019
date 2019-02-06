import unittest
from Calculadora import calculadora

class testCalculadora(unittest.TestCase):

    def test_suma_2_mas_2(self):
        calc = calculadora()
        self.assertEquals(4, calc.suma(2,2))
    
    def test_suma_5_mas_10(self):
        calc = calculadora()
        self.assertEquals(15, calc.suma(5,10))
    
    def test_suma_menos_5_mas_10(self):
        calc = calculadora()
        self.assertEquals(5, calc.suma(-5,10))

if __name__ == "__main__":
    unittest.main()

