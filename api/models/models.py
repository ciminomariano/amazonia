from typing import Tuple, List, Optional

from pydantic.main import BaseModel


class ChessboardCoordinate:
    def __init__(self, row: int, column: str):
        self.row = row
        self.column = column

    def to_tuple(self) -> Tuple[int, str]:
        return self.row, self.column


class Drone:
    def __init__(self, position: ChessboardCoordinate):
        self.position = position


class DeliveryOut:
    def __init__(self, start: str, pickup: str, destination: str, route: List[str], time: int):
        self.start = start
        self.pickup = pickup
        self.destination = destination
        self.route = route
        self.time = time


class Object:
    def __init__(self, position: ChessboardCoordinate):
        self.position = position


class Destination:
    def __init__(self, position: ChessboardCoordinate):
        self.position = position


class DeliveryCreate:
    def __init__(self, start: str, pickup: str, destination: str, objects: List[Object]):
        self.start = start
        self.pickup = pickup
        self.destination = destination
        self.objects = objects


class DeliveryInDB(BaseModel):
    id: str
    start: str
    pickup: str
    destination: str
    route: Optional[str]
    time: Optional[float]
