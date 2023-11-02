from src.ejercicio4 import ordenMenorMayor
import pytest

def test_ordenMenorMayor():
    assert ordenMenorMayor([5,2,8,1]) == [1,2,5,8]