from src.ejercicio9 import vecesVocal
import pytest


@pytest.mark.parametrize(
    "palabra, vocal, expected",
    [
        ("hola", "a", 1),
        ("esto es una prueba", "e", 3),
    ]
)

def test_vecesVocal(palabra,vocal,expected):
    assert vecesVocal(palabra,vocal) == expected