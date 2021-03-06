from .vector import Vector
from .number import Number


class NumberVector(Vector):
    """Define a parameter accepting a list of numbers.

    >>> @argument('value', types.NumberVector, min=10, max=100, step=10)
    ... def func(value=(10, 11)):
    ...     pass
    """

    paramType = 'number-vector'
    elementClass = Number
