import pytest
from .plant import Plant

def test_getMoistness():
    p = Plant()
    assert p.getMoistness() == 0
