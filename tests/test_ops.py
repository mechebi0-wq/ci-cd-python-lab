import math
import pytest
from calc import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(4, 3) == 12

def test_div():
    assert math.isclose(div(9, 4), 2.25)

@pytest.mark.parametrize("a,b", [(1,0), (-3,0)])
def test_div_zero(a,b):
    with pytest.raises(ZeroDivisionError):
        div(a,b)