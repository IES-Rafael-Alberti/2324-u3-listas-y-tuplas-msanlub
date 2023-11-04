from src.ejercicio13 import calculoMedia,calculoDesviacionTipica
import pytest

def test_calculoMedia():
    assert calculoMedia([1,2,3,4,5]) == 3.0

def test_calculoDesviacionTipica():
    assert calculoDesviacionTipica([1,2,3,4,5],3.0) == 1.4142135623730951