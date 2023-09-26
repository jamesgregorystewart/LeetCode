""" 875 MEDIUM Koko Eating Bananas """

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.
#
#  
#
# Example 1:
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#  
#
# Constraints:
#
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

"""
Idea:
    - binary search for rate value that yields the hours to eat all the bananas we want
    - final loop to check if we can reduce rate by a couple points
Time: O(nlog(n))
Space: (1)
"""

from typing import List
from math import ceil
from functools import reduce

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            rate = ((low + high) // 2) 
            hours_to_eat = reduce(lambda hours, pile: hours + ceil(pile / rate), piles, 0)
            if hours_to_eat == h:
                break
            elif hours_to_eat < h:
                high = rate - 1
            else:
                low = rate + 1
        if hours_to_eat != h:
            return low
        while hours_to_eat == h: 
            if rate == 1:
                return rate
            rate -= 1
            hours_to_eat = reduce(lambda hours, pile: hours + ceil(pile / rate), piles, 0)
        return rate + 1

solution = Solution()
print(solution.minEatingSpeed([3,6,7,11], 8))
print(solution.minEatingSpeed([30,11,23,4,20], 5))
print(solution.minEatingSpeed([30,11,23,4,20], 6))
print(solution.minEatingSpeed([312884470], 312884469))
print(solution.minEatingSpeed([873375536,395271806,617254718,970525912,634754347,824202576,694181619,20191396,886462834,442389139,572655464,438946009,791566709,776244944,694340852,419438893,784015530,588954527,282060288,269101141,499386849,846936808,92389214,385055341,56742915,803341674,837907634,728867715,20958651,167651719,345626668,701905050,932332403,572486583,603363649,967330688,484233747,859566856,446838995,375409782,220949961,72860128,998899684,615754807,383344277,36322529,154308670,335291837,927055440,28020467,558059248,999492426,991026255,30205761,884639109,61689648,742973721,395173120,38459914,705636911,30019578,968014413,126489328,738983100,793184186,871576545,768870427,955396670,328003949,786890382,450361695,994581348,158169007,309034664,388541713,142633427,390169457,161995664,906356894,379954831,448138536], 943223529))
print(solution.minEatingSpeed([312884470],968709470))
print(solution.minEatingSpeed([3,6,7,11], 18))
print(solution.minEatingSpeed([2,2], 4))
