from re import S
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heater = 0
        heaters = [float("-inf")] + heaters + [float("inf")]
        radius = float("-inf")
        for house in houses:
            while house >= heaters[heater]:
                heater += 1
            radius = max(
                radius,
                min(abs(house - heaters[heater]), abs(house - heaters[heater - 1])),
            )

        return radius
