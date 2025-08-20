from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError


class Calculator3:
    def __init__(self, driver_handler: DriverHandleInterface) -> None:
        self.__driver_handle = driver_handler

    def calculate(self, request: FlaskRequest) -> None:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_results(variance, multiplication)

        return self.__format_response(variance)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handle.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num

        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:

        if variance < multiplication:
            raise HttpBadRequestError(
                "Falha no processo, variância menor que multiplicação")

    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "result": variance,
                "Success": True
            }
        }
