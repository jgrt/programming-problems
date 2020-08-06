"""
https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0

The cost of stock on each day is given in an array A[] of size N.
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
Return (buy_day, sell_day) for profit, return "No Profit" if there is no profit.

Constraints:
2 <= N <= 10^3
0 <= Ai <= 10^4

Input: N = 7,  arr = 100 180 260 310 40 535 695
Output: (0 3) (4 6)
"""
from pydantic import BaseModel, Field, validator
from typing import List, Tuple, Union


class ConstrainedArray(BaseModel):
    array: List[int] = Field(..., min_items=2, max_items=1000)

    @validator('*', pre=True, each_item=True)
    def element_must_be_in_range(cls, v):
        assert 0 <= v <= pow(10, 4),  'must be in range {}'.format([0, pow(10, 4)])
        return v


def stock_buy_and_sell(arr: List[int]) -> Union[List[Tuple[int, int]], str]:
    n = len(arr)
    if arr == sorted(arr, reverse=True):
        return 'No Profit'
    buy_sell = list()
    for i in range(n-1, 0, -1):
        arr[i] = arr[i] - arr[i-1]
    arr[0] = -arr[0]
    arr = arr + [-100]
    for idx in range(1, n+1):
        if (arr[idx] > 0) and (arr[idx - 1] < 0):
            buy = idx - 1
        if (arr[idx] < 0) and (arr[idx - 1] > 0):
            sell = idx - 1
            buy_sell.append((buy, sell))

    return buy_sell


if __name__ == '__main__':
    # array = [100, 180, 260, 310, 40, 535, 695]
    array = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
    ConstrainedArray(array=array)
    print(stock_buy_and_sell(array))
