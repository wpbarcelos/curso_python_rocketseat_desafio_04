from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from typing import Dict, List
from pytest import raises

from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandleInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3


def test_calculate_integration():

    mock_request = MockRequest({"numbers": [2.12, 4.16, 1.32]})
    calculator2 = Calculator2(NumpyHandler())
    formatted_response = calculator2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'Calculator': 2, 'result': 0.09}}


def test_calculate():

    mock_request = MockRequest({"numbers": [2.12, 4.16, 1.32]})
    calculator2 = Calculator2(MockDriverHandler())
    formatted_response = calculator2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {'data': {'Calculator': 2, 'result': 0.33}}
