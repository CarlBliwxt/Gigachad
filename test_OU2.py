"""
Unit tests for the mandatory assignments in lesson 6.

Instructions:
    - make sure you've installed `pytest` and `numpy` on your computer.
    - replace `OU2` on line 17 by the name of the file containing your functions
    - in the terminal run `pytest test_OU2.py` or `pytest-3 test_OU2.py` (make sure pytest uses python 3!)

More documentation about pytest is available on docs.pytest.org
"""

import pytest
import numpy as np
import numpy.linalg as npl

# Change OU2 by the name of the file containing your functions
from Assignment2_1_2 import *

@pytest.fixture
def x():
    return [1, 2, 6, 4, 5, 0, 1, 2]

@pytest.fixture
def y():
    return [1 for _ in range(100)]

def test_smooth_a(x, y):
    assert smooth_a([], 10) == []

    assert smooth_a(x, 0) == x
    assert smooth_a(x, 1) == [1.3333333333333333, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.6666666666666667]
    assert smooth_a(x, 2) == [2.2, 2.8, 3.6, 3.4, 3.2, 2.4, 2.0, 1.4]
    assert len(smooth_a(x, 10)) == len(x)
    assert smooth_a(y, 20) == y



def test_round_list(x, y):
    assert round_list(smooth_a(x, 1), 2) == [1.33, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.67]

    assert round_list(x, 3) == x
    assert round_list(y, 3) == y
