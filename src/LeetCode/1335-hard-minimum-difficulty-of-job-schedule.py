# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
#
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.
#
# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
#
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
#
#
#
# Example 1:
#
#
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7
# Example 2:
#
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
# Example 3:
#
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.
#
#
# Constraints:
#
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10

"""
States:
1) min job difficult from the ith day
2) days remaining for jobs to be scheduled

At each state we need to iterate over all possible days which can be included.
"""


from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        # To set the base cases we need a 0 in last column for each row
        dp = [[float("inf")] * (d) + [0] for _ in range(len(jobDifficulty))]
        """
        Base Case; if d == day, min val for last day is 
        equal to the max val in remaining range jobs[i:]; In other words..

        On the last day, we must schedule all remaining jobs, so 
        dp[i][d] is the max difficulty job remaining
        """
        dp[-1][d] = jobDifficulty[-1]
        for i in range(len(jobDifficulty) - 2, -1, -1):
            dp[i][d] = max(dp[i + 1][d], jobDifficulty[i])

        for day in range(d - 1, 0, -1):
            for i in range(day - 1, len(jobDifficulty) - d + day):
                hardest = 0
                for j in range(i, len(jobDifficulty) - d + day):
                    hardest = max(hardest, jobDifficulty[j])
                    dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

        return -1 if dp[0][1] == float("inf") else int(dp[0][1])


solution = Solution()
print(solution.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
print(solution.minDifficulty(jobDifficulty=[9, 9, 9], d=4))
print(solution.minDifficulty(jobDifficulty=[1, 1, 1], d=3))
print(solution.minDifficulty(jobDifficulty=[6, 5, 10, 3, 2, 1], d=3))
print(solution.minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6))
