# Greedy

Solving Greedy problems typically involves the identification and use of an invariant. Some variable or variables which are maintained over the course of program execution which helps decision making at each step.

Examples:
[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
The invariant in this problem is `cur_sum` which you maintain as you iterate through the array. Here, if cur_sum + nums[i] is greater than nums[i], then extend that sum through nums[i]. If nums[i] is greater than cur_sum + nums[i], then set cur_sum to nums[i].

A tricky greedy example:
[Jump Game II](https://leetcode.com/problems/jump-game-ii/)


