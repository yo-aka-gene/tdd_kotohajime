"""
ABC Class of Algebra
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class _Algebra(ABC):
  """
  ABC Class of Algebra

  Method
  ------
  compute(**args: Dict[str, Any]) -> Any
  """

  @abstractmethod
  def __init__(self, **kwargs: Dict[str, Any]):
    """
    Parameters
    ----------
    kwargs: Dict[str, Any]
      generate method options of each Alg
    """
    pass

  @abstractmethod
  def compute(self, **args: Dict[str, Any]) -> Any:
    """
    Parameters
    ----------
    args: Dict[str, Any]
      it is expected to contain the followings

      1. x: Any
        1st argument
      2. y: Any
        2nd argument

    Return
    ------
    value: Any
      return value of the calculation
    """
    pass
