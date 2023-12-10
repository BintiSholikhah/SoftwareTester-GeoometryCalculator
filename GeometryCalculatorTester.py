import unittest
from geometry_calculator import GeometryCalculator

class GeometryCalculatorTester(unittest.TestCase):

    #arrange
    def setUp(self):
        self.alas = 4
        self.tinggi = 7
        self.sisi = 5
        self.jari = 10

    def test_luas_segitiga(self):
        #act
        actualResult = GeometryCalculator.luas_segitiga(self.alas, self.tinggi)
        #assert
        expectedResult = 0.5 * self.alas * self.tinggi
        self.assertEqual(actualResult, expectedResult)

    def test_luas_kubus(self):
        #act
        actualResult = GeometryCalculator.luas_kubus(self.sisi)
        #assert
        expectedResult = self.sisi * self.sisi
        self.assertEqual(actualResult, expectedResult)
    
    def test_luas_lingkaran(self):
        #act
        actualResult = GeometryCalculator.luas_lingkaran(self.jari)
        #assert
        expectedResult = 3.14 * self.jari * self.jari
        self.assertEqual(actualResult, expectedResult)
    
    def test_jajar_genjang(self):
        #act
        actualResult = GeometryCalculator.jajar_genjang(self.alas, self.tinggi)
        #assert
        expectedResult = self.alas * self.tinggi
        self.assertEqual(actualResult, expectedResult)
    
    def test_keliling_lingkaran(self):
        #act
        actualResult = GeometryCalculator.keliling_lingkaran(self.jari)
        #assert
        expectedResult = 3.14 * (2 * self.jari)
        self.assertEqual(actualResult, expectedResult)
    
    def test_diameter_lingkaran(self):
        #act
        actualResult = GeometryCalculator.diameter_lingkaran(self.jari)
        #assert
        expectedResult = self.jari + self.jari
        self.assertEqual(actualResult, expectedResult)

unittest.main() #vscode