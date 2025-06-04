"""Test cases de la clase membership
"""
import unittest
from membership import is_valid_plan, is_valid_feature, get_plan_details

class TestMembership(unittest.TestCase):
    """Clase TestCalculator

    Args:
        unittest (TestCase): recibe el unittest con la clase a realizar el test
    """
    def test_valid_plan(self):
        """Test case para verificar si el plan es válido
        """
        self.assertTrue(is_valid_plan("Basic"))

    def test_invalid_plan(self):
        """Test case para verificar si el plan es inválido
        """
        self.assertFalse(is_valid_plan("InvalidPlan"))

    def test_valid_feature(self):
        """Test case para verificar si las funcionalidades de plan son validas
        """
        self.assertTrue(is_valid_feature("Basic", "Group Classes"))

    def test_invalid_feature(self):
        """Test case para verificar las funcionalidades de plan son inválidas
        """
        self.assertFalse(is_valid_feature("Premium", "InvalidFeature"))

    def test_get_plan_details(self):
        """Test case para obtener los detalles del plan seleccionado
        """
        self.assertIsInstance(get_plan_details("Family"), dict)

if __name__ == "_main_":
    unittest.main()
