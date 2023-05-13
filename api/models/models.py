from typing import Tuple, List, Optional

from pydantic import BaseModel


class ChessboardCoordinate:
    def __init__(self, row: int, column: str):
        self.row = row
        self.column = column

    def to_tuple(self) -> Tuple[int, str]:
        return self.row, self.column


class Drone:
    def __init__(self, position: ChessboardCoordinate):
        self.position = position


class DeliveryOut(BaseModel):
    id: Optional[str]
    start: str
    pickup: str
    destination: str
    route: str
    time: int


class Object:
    def __init__(self, position: ChessboardCoordinate):
        self.position = position


class Destination:
    def __init__(self, position: ChessboardCoordinate):
        self.position = position


class Config:
    arbitrary_types_allowed = True


class Object:
    # your Object model definition here
    pass


class DeliveryCreate(BaseModel):
    start: str
    pickup: str
    destination: str
    description: Optional[str]

    class Config:
        arbitrary_types_allowed = True


class DeliveryInDB(BaseModel):
    id: str
    start: str
    pickup: str
    destination: str
    route: Optional[str]
    time: Optional[float]
