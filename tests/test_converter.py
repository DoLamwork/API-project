import unittest
from app.core.converter import gross_to_net, net_to_gross

class TestConverter(unittest.TestCase):

    def test_gross_to_net(self):
        result = gross_to_net(20000000, num_dependents=1)
        self.assertAlmostEqual(result["net"], 17775000, delta=1000)
        self.assertEqual(round(result["bhxh"]), 1600000)
        self.assertEqual(round(result["bhyt"]), 300000)
        self.assertEqual(round(result["bhtn"]), 200000)
        self.assertGreaterEqual(result["taxable_income"], 0)

    def test_net_to_gross(self):
        result = net_to_gross(17900000, num_dependents=1)
        self.assertAlmostEqual(result["net"], 17900000, delta=1000)
        self.assertGreaterEqual(result["gross"], 17900000)

if __name__ == "__main__":
    unittest.main()
