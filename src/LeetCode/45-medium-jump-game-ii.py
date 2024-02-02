# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_far = cur_end = ans = 0
        for i in range(len(nums) - 1):
            # farthest we can go is from our position to max jump available from that position
            cur_far = max(cur_far, i + nums[i])
            # when i hits cur_end, we have hit the boundary of a previous jump,
            # and a new jump is required to make it to the farthest point we know we can reach;
            # so we set the next end to far, and increment ans
            if i == cur_end:
                cur_end = cur_far
                ans += 1
        return ans


solution = Solution()
print(solution.jump(nums=[2, 3, 1, 1, 4]))
print(solution.jump(nums=[2, 3, 0, 1, 4]))
print(solution.jump(nums=[1, 1, 1, 1]))
