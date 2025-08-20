from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from typing import Dict, List
from pytest import raises

from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError(DriverHandleInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

    def variance(self, numbers: List[float]) -> float:
        return 3


class MockDriverHandler(DriverHandleInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

    def variance(self, numbers: List[float]) -> float:
        return 1000000


def test_calculate_variance_with_error():

    with raises(Exception) as exinfo:
        mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
        calculator3 = Calculator3(MockDriverHandlerError())
        calculator3.calculate(mock_request)

    error_message = "Falha no processo, variância menor que multiplicação"
    assert str(exinfo.value) == error_message


def test_calculate_variance_integration():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator3 = Calculator3(MockDriverHandler())
    response = calculator3.calculate(mock_request)
    assert response == {'data': {'Calculator': 3,
                                 'result': 1000000, 'Success': True}}


def test_calculate_variance():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator3 = Calculator3(MockDriverHandler())
    response = calculator3.calculate(mock_request)

    assert response == {'data': {'Calculator': 3,
                                 'result': 1000000, 'Success': True}}
