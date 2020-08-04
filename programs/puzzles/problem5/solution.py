"""
https://practice.geeksforgeeks.org/problems/angle-between-hour-and-minute-hand/0

Calculate the angle between hour hand and minute hand.
There can be two angles between hands, we need to print minimum of two.
Also, we need to return floor of final result angle. For example, if the final angle is 10.61, we need to return 10.

Constraints:
1 ≤ h ≤ 12
1 ≤ m ≤ 60

Input: h = 3, m = 30
Output: 75
"""
from pydantic import BaseModel, Field
from math import floor


class ConstrainedIntegers(BaseModel):
    hour: int = Field(..., ge=1, le=12)
    minute: float = Field(..., ge=1, le=60)


def angle_bw_hour_minute_hand(h: int, m: float) -> int:
    if m == 60:
        h -= 1
    hour_hand = h * 30 + m * .5
    minute_hand = m * 6
    angle1 = abs(hour_hand - minute_hand)
    angle2 = 360 - angle1
    return floor(min(angle1, angle2))


if __name__ == '__main__':
    hour = 6
    minute = 33.8151
    constrained_values = ConstrainedIntegers(hour=hour, minute=minute)
    print(angle_bw_hour_minute_hand(constrained_values.hour, constrained_values.minute))
