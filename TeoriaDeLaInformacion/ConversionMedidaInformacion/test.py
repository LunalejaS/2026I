import unittest
import math
from main import info_units_conversion

class TestInfoUnitsConversion(unittest.TestCase):

    def test_same_unit(self):
        self.assertEqual(info_units_conversion("bit", "bit", 5), 5)

    def test_bit_to_nat(self):
        result = info_units_conversion("bit", "nat", 1)
        self.assertAlmostEqual(result, math.log(2), places=5)

    def test_bit_to_hartley(self):
        result = info_units_conversion("bit", "hartley", 1)
        self.assertAlmostEqual(result, math.log10(2), places=5)

    def test_nat_to_bit(self):
        result = info_units_conversion("nat", "bit", 1)
        self.assertAlmostEqual(result, math.log2(math.e), places=5)

    def test_hartley_to_bit(self):
        result = info_units_conversion("hartley", "bit", 1)
        self.assertAlmostEqual(result, math.log2(10), places=5)

    def test_plural_and_case(self):
        result = info_units_conversion("BITS", "NATS", 1)
        self.assertAlmostEqual(result, math.log(2), places=5)

if __name__ == "__main__":
    unittest.main()