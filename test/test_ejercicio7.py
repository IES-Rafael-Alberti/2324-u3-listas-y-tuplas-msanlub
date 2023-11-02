from src.ejercicio7 import multiploTres
import pytest

def test_multiploTres():
    assert multiploTres(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]) == ['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'ñ', 'p', 'q', 's', 't', 'v', 'w', 'y', 'z']