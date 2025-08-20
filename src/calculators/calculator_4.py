from flask import request as FlaskRequest
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict, List

from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface


class Calculator4:

    def __init__(self, driver_handler: DriverHandleInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> float:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        average = self.__average(input_data)
        return self.__format_response(average)

    def __validate_body(self, body: Dict) -> List[float]:

        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        return body["numbers"]

    def __average(self, numbers: List[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": average,
                "Success": True
            }
        }
