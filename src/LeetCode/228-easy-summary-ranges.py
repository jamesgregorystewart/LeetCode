from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        segment: List[int] = []
        for num in nums:
            if segment and abs(segment[-1] - num) > 1:
                ans.append(
                    "->".join(
                        [
                            str(x)
                            for i, x in enumerate(segment)
                            if i in [0, len(segment) - 1]
                        ]
                    )
                )
                segment = []
            segment.append(num)
        if segment:
            ans.append(
                "->".join(
                    [
                        str(x)
                        for i, x in enumerate(segment)
                        if i in [0, len(segment) - 1]
                    ]
                )
            )
        return ans


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        a = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] > 1:
                if nums[i - 1] == a:
                    ans.append(str(a))
                else:
                    ans.append("->".join([str(a), str(nums[i - 1])]))
                a = nums[i]
            if i == len(nums) - 1:
                if nums[i] == a:
                    ans.append(str(a))
                else:
                    ans.append("->".join([str(a), str(nums[i])]))
            i += 1
        return ans
