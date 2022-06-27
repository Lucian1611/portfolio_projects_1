import unittest
import main

class TestLectia7(unittest.TestCase):
    def test_valori(self):
        parametru_de_testare = 8.4
        rezultat = main.celsius_to_farenheight(parametru_de_testare)
        self.assertEqual(rezultat, 47.12)

    def test_valori2(self):
        parametru_de_testare = 0
        rezultat = main.celsius_to_farenheight(parametru_de_testare)
        self.assertEqual(rezultat, 32)

if __name__ == "__main__":
    unittest.main()
