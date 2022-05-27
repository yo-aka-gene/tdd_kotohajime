"""
Test for Sum Module
"""

import numpy as np
import pytest

from tdd.zalg import Sum
from typing import Callable

@pytest.fixture
def correct_input():
  return np.arange(-10, 10)

@pytest.fixture
def invalid_input():
  return [None, "5", 0.5, 1.00, lambda x: x, 10e5, 3 + 5j]

def test_init_instance():
  model = Sum()
  assert isinstance(model.func, Callable), \
    f"self.func expected Callable, got {model.func}"

def test_compute_invalid_x(invalid_input):
  model = Sum()
  for x in invalid_input:
    with pytest.raises(AssertionError) as e:
      model.compute(x, 0)
    assert f"{x}" in f"{e.value}", \
      f"NoReasons: Inform the AssertionError reasons, got {e.value}"

def test_compute_invalid_y(invalid_input):
  model = Sum()
  for y in invalid_input:
    with pytest.raises(AssertionError) as e:
      model.compute(0, y)
    assert f"{y}" in f"{e.value}", \
      f"NoReasons: Inform the AssertionError reasons, got {e.value}"
