import unittest
from membership import is_valid_plan, is_valid_feature, get_plan_details

class TestMembership(unittest.TestCase):
    def test_valid_plan(self):
        self.assertTrue(is_valid_plan("Basic"))

    def test_invalid_plan(self):
        self.assertFalse(is_valid_plan("InvalidPlan"))

    def test_valid_feature(self):
        self.assertTrue(is_valid_feature("Basic", "Group Classes"))

    def test_invalid_feature(self):
        self.assertFalse(is_valid_feature("Premium", "InvalidFeature"))

    def test_get_plan_details(self):
        self.assertIsInstance(get_plan_details("Family"), dict)

if __name__ == "_main_":
    unittest.main()