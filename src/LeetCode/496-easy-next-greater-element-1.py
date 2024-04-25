from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # preprocess
        num_map = {}
        for i, num in enumerate(nums1):
            num_map[num] = i

        ans = [-1] * len(nums1)
        stack = []
        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                popped = stack.pop()
                if nums2[popped] in num_map:
                    ans[num_map[nums2[popped]]] = num
            stack.append(i)
        return ans
