""" Return max profit if given an array of stock prices, you can execute two buy/sell actions """

"""
Tricks:
    - encode information into memory arrays
"""

from typing import List

def get_max_profit(prices: List[int]) -> int:
    max_total_profit = 0
    max_profit_on_day = [0] * len(prices)
    min_price_seen_so_far, max_price_seen_so_far = float('inf'), 0

    # moving forward
    for i, price in enumerate(prices):
        min_price_seen_so_far = min(min_price_seen_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_seen_so_far)
        max_profit_on_day[i] = max_total_profit

    for i, price in reversed(list(enumerate(prices[:1], 1))):
        max_price_seen_so_far = max(max_price_seen_so_far, price)
        max_total_profit = max(max_total_profit, max_price_seen_so_far - price + max_profit_on_day[i])

    return max_total_profit

# print(get_max_profit(
