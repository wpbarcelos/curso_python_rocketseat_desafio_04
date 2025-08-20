
from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler


def calculator3_factory() -> Calculator3:
    calc = Calculator3(NumpyHandler())
    return calc
