from __future__ import annotations

import math


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def create_from_location(cls, location: list[int]) -> Point:
        return cls(x=location[0], y=location[1])

    def calculate_distance_to(self, destination: Point) -> float:
        return math.sqrt(
            math.pow(destination.x - self.x, 2) + math.pow(destination.y - self.y, 2)
        )
