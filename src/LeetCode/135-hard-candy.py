# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.
#
#
#
# Example 1:
#
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
#
#
# Constraints:
#
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = 0
        begin = end = -1
        n = len(ratings)
        for i in range(len(ratings)):
            # find a "1" then work backwards to "end"; then reset end to "i"
            if isBottom(ratings, i):
                begin = i
                candies += 1
            else:
                for j in range(begin, end)

        return 0

    def isBottom(self, ratings: List[int], i: int) -> bool:
        n = len(ratings)
        if i == 0 and i < n - 1 and ratings[i] < ratings[i + 1]:
            return True
        if i == n - 1 and n > 1 and ratings[i] < ratings[i - 1]:
            return True
        if n == 1:
            return True
        if (
            i > 0
            and i < n - 1
            and ratings[i - 1] >= ratings[i]
            and ratings[i] <= ratings[i + 1]
        ):
            return True
        return False
