from typing import Dict
from pytest import raises
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface

from .calculator_4 import Calculator4


class MockDriverHandler(DriverHandleInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        pass

    def variance(self, numbers: List[float]) -> float:
        pass

    def average(self, numbers: List[float]) -> float:
        total = sum(numbers)
        count = len(numbers)
        return total / count


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calcule_with_error():
    with raises(Exception) as exinfo:
        bad_request = MockRequest({"noob": [1, 2, 3, 4]})
        calculate4 = Calculator4(MockDriverHandler())
        calculate4.calculate(bad_request)

    assert str(exinfo.value) == "body mal formatado!"


def test_calculate():
    mock_request = MockRequest({"numbers": [4, 6, 8, 10]})
    calculate4 = Calculator4(MockDriverHandler())
    response = calculate4.calculate(mock_request)

    assert response == {
        "data": {
            "Calculator": 4,
            "result": 7.0,
            "Success": True
        }
    }
