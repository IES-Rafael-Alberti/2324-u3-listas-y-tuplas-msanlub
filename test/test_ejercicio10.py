from src.ejercicio10 import numeroMayor,numeroMenor
import pytest

@pytest.mark.parametrize(
    "numeros, expected",
    [
        ([50, 75, 46, 22, 80, 65, 8], 80)
    ]
)

def test_numeroMayor(numeros,expected):
    assert numeroMayor(numeros) == expected

@pytest.mark.parametrize(
    "numeros, expected",
    [
        ([50, 75, 46, 22, 80, 65, 8], 8)
    ]
)

def test_numeroMenor(numeros,expected):
    assert numeroMenor(numeros) == expected