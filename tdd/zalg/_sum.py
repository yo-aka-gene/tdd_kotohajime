"""Main module."""
from tdd.type import _Algebra as Algebra

class Sum(Algebra):
  """
  Algebra Class Summation on Integers

  Method
  ------
  compute(self, x: int, y: int) -> int
  """

  def __init__(self):
    self.func = lambda x, y: x + y
  
  def compute(self, x: int, y: int) -> int:
    """
    Return summation of integers

    Parameters
    ----------
    x: int
      1st argument
    y: int
      2nd argument
    
    Return
    ------
    value: int

    Example
    -------
    >>> from tdd.zalg import Sum
    >>> algebra = Sum()
    >>> algebra.compute(x=5, y=3)
    8
    """
    assert isinstance(x, int), \
      f"Invalid input: x expected int, got {x}"
    assert isinstance(y, int), \
      f"Invalid input: y expected int, got {y}"
    return self.func(x, y)
