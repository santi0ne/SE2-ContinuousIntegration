# test_calculator.py
import unittest
from calculator import calculate_total_cost

class TestCalculator(unittest.TestCase):
    def test_base_cost(self):
        plan = {"name": "Basic", "base_cost": 50, "features": {"Group Classes": 20}}
        self.assertEqual(calculate_total_cost(plan, ["Group Classes"]), 70)

    def test_group_discount(self):
        plan = {"name": "Basic", "base_cost": 100, "features": {}}
        self.assertEqual(calculate_total_cost(plan, [], group_members=2), 90)

    def test_special_discount(self):
        plan = {"name": "Basic", "base_cost": 210, "features": {}}
        self.assertEqual(calculate_total_cost(plan, []), 190)

    def test_premium_surcharge(self):
        plan = {"name": "Premium", "base_cost": 200, "features": {"Personal Trainer": 50}}
        expected_total = int(round((200 + 50) * 1.15)) - 20  # se aplica también el descuento de $20
        self.assertEqual(calculate_total_cost(plan, ["Personal Trainer"]), expected_total)

if __name__ == "__main__":
    unittest.main()
