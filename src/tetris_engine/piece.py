from enum import Enum
from typing import List


class Shape(Enum):
    Q = [[1, 1], [1, 1]]

    Z = [[1, 1, 0], [0, 1, 1]]

    S = [[0, 1, 1], [1, 1, 0]]

    T = [[1, 1, 1], [0, 1, 0]]

    I = [[1, 1, 1, 1]]

    L = [[1, 0], [1, 0], [1, 1]]

    J = [[0, 1], [0, 1], [1, 1]]


class Piece:

    CHAR = "O"

    def __init__(self, shape_letter: str):
        self.shape = Shape[shape_letter]

    def shape(self) -> Shape:
        return self.shape

    def shape(self, shape_letter: str) -> Shape:
        return Shape[shape_letter]

    def get(self) -> List[List[int]]:
        return self.shape.value
