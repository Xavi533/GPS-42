"""
Este módulo contiene pruebas unitarias para verificar las funciones de transformación de texto.
"""

import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """Clase de pruebas unitarias para las funciones de transformación de cadenas."""

    def test_is_upper(self):
        """Prueba si la función to_upper_case transforma correctamente el texto a mayúsculas."""
        string = transform.to_upper_case("hello")
        self.assertEqual(string, "HELLO")

    def test_is_lower(self):
        """Prueba si la función to_lower_case transforma correctamente el texto a minúsculas."""
        string = transform.to_lower_case("HELLO")
        self.assertEqual(string, "hello")

    def test_is_capitalize(self):
        """Prueba si la función to_capitalize transforma correctamente el texto a capitalizado."""
        string = transform.to_capitalize("HELLO")
        self.assertEqual(string, "Hello")


if __name__ == '__main__':
    unittest.main()
