"""
Test for Multiplicate Module
"""

import numpy as np
import pytest

from tdd.zalg import Multiplicate as Mult
from typing import Callable


@pytest.fixture
def correct_input():
  return np.random.randint(-100, 100, (10, 2))


@pytest.fixture
def invalid_input():
  return [None, "5", 0.5, 1.00, lambda x: x, 10e5, 3 + 5j]


def test_init_instance():
  model = Mult()
  assert isinstance(model.func, Callable), \
    f"self.func expected Callable, got {model.func}"


def test_compute_invalid_x(invalid_input):
  model = Mult()
  for x in invalid_input:
    with pytest.raises(AssertionError) as e:
      model.compute(x, 0)
    assert f"{x}" in f"{e.value}", \
      f"NoReasons: Inform the AssertionError reasons, got {e.value}"


def test_compute_invalid_y(invalid_input):
  model = Mult()
  for y in invalid_input:
    with pytest.raises(AssertionError) as e:
      model.compute(0, y)
    assert f"{y}" in f"{e.value}", \
      f"NoReasons: Inform the AssertionError reasons, got {e.value}"


def test_compute_correct_input(correct_input):
  model = Mult()
  for xy in correct_input:
    x, y = (xy[0].item(), xy[1].item())
    exp = x * y
    assert model.compute(x, y) == exp, \
      f"self.compute is expected to retrun summation of arguments, \
        got {model.compute(x, y)} while x:{x}[{type(x)}] y:{y}[{type(y)}]"
