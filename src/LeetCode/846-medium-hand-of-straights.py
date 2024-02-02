# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
#
#
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:
#
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
#
#
#
# Constraints:
#
# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length


from typing import List
import heapq
import collections


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counts = collections.Counter(hand)
        heapq.heapify(hand)
        while hand:
            while hand and counts[hand[0]] == 0:
                heapq.heappop(hand)
            if not hand:
                return True
            card = heapq.heappop(hand)
            for i in range(card, card + groupSize):
                if i not in counts or counts[i] == 0:
                    return False
                counts[i] -= 1
        return True


solution = Solution()
print(solution.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
print(solution.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4))
