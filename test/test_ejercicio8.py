from src.ejercicio8 import comprobarPalindromo
import pytest

def test_comprobarPalindromo():
    assert comprobarPalindromo("arañara") == True