from src.ejercicio11 import calculoProductoEscalar
import pytest

@pytest.mark.parametrize(
    "vectorUno,vectorDos, expected",
    [
        ([1,2,3],[-1,0,2], 5)
    ]
)

def test_calculoProductoEscalar(vectorUno,vectorDos,expected):
    assert calculoProductoEscalar(vectorUno,vectorDos) == expected