""" Return max profit if given an array of stock prices, you can execute two buy/sell actions """

"""
Tricks:
    - encode information into memory array.
    - First pass is left to right, calculating max profit possible with one buy/sell, encoded into an array by day; 
        Track minimum price seen, max_profit_first_day, and saving max_profit_first_day into prices[i].
    - Second pass is right to left, calculating max profit possible with a second buy/sell by tracking
        largest price seen, and saving 
            max_total_profit = max(max_total_profit, (largest_price_seen - prices[i]) + max_profit_first_day[i])
"""

from typing import List

def get_max_profit_buy_sell_twice(prices: List[int]) -> int:
    # First pass is forward to calculate max first day buy/sell profit
    min_price_seen = float('inf')
    max_profit_first_day = 0
    max_first_trade_profit_by_day = [0] * len(prices)
    for i, price in enumerate(prices):
        max_profit_first_day = max(max_profit_first_day, price - min_price_seen)
        min_price_seen = min(min_price_seen, price)
        max_first_trade_profit_by_day[i] = max_profit_first_day

    # Second pass is backwards, calculating max total profit, referencing first day's profits
    max_total_profit, largest_price_seen = 0, prices[len(prices)-1]
    for i, price in reversed(list(enumerate(prices))):
        max_total_profit = max(max_total_profit, (largest_price_seen - price) + max_first_trade_profit_by_day[i])
        largest_price_seen = max(largest_price_seen, price)

    return max_total_profit


print(get_max_profit_buy_sell_twice([12,11,13,9,12,8,14,13,15]))
print(get_max_profit_buy_sell_twice([0,1]))

