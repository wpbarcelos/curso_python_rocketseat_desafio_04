import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverHandleInterface


class NumpyHandler(DriverHandleInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)

    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)

    def avg(self, numbers: List[float]) -> float:
        self.__np.average(numbers)
