from src.ejercicio1 import *
import pytest

def test_guardaAsignatura():
    assert guardaAsignatura("Matemáticas") == ["Matemáticas"]