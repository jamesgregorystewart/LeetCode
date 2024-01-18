# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
#
#  
#
# Example 1:
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
#
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#  
#
# Constraints:
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.

from typing import List, Tuple


class Solution:
    def calcEquation(
            self,
            equations: List[List[str]],
            values: List[float],
            queries: List[List[str]]) -> List[float]:

        gid_weight = {}

        def find(node_id: str) -> Tuple[str, float]:
            """
            This will find the gid of the node and that node's weight
            It will lazily update the gid to that of the divisor and
            it will update the weight per the chain
            """
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]

            if group_id != node_id:
                # trigger chain update
                # dividends will share common, terminal divisor
                # node weight will be multiplied up the chain
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    new_group_id, node_weight * group_weight
            return gid_weight[node_id]

        def union(dividend: str, divisor: str, value: float) -> None:
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # we must merge two groups
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight * value / dividend_weight)

        # Step 1: Build the graph with weights
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        # Step 2: Compute the queries and lazily update gid/weight mappings
        results = []
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # they are not in the same group
                    results.append(-1.0)
                else:
                    results.append(dividend_weight / divisor_weight)
        return results


solution = Solution()
print(solution.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
