# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
#
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
#
#  
#
# Example 1:
#
#
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# Example 2:
#
#
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
#  
#
# Constraints:
#
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi

from typing import List, Set, Tuple, Dict
import collections

# MY Solution I worked so hard on
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         # FIRST we sort the tickets we have to evaluate them in lex order
#         sorted_tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
#
#         # SECOND create adjacency list
#         ticket_graph = collections.defaultdict(list)
#         for source, dest in sorted_tickets:
#             ticket_graph[source].append(dest)
#
#         def dfs(
#                 source: str,
#                 itinerary: List[str],
#                 flights: int,
#                 counter: Dict[tuple[str, str], int]):
#             if len(itinerary) == len(tickets) + 1:
#                 return itinerary.copy()
#             for dest in ticket_graph[source]:
#                 ticket = (source, dest)
#                 if counter[ticket] > 0:
#                     itinerary.append(dest)
#                     counter[ticket] -= 1
#                     valid_itinerary = dfs(dest, itinerary, flights+1, counter)
#                     if valid_itinerary:
#                         return valid_itinerary
#                     itinerary = itinerary[:-1]
#                     counter[ticket] += 1
#             return []
#         print(collections.Counter([tuple(ticket) for ticket in tickets]))
#         return dfs("JFK", ["JFK"], collections.Counter([tuple(ticket) for ticket in tickets]))


class Solution(object):
    def findItinerary(self, tickets):
        self.flightMap = collections.defaultdict(list)

        for origin, dest in tickets:
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)


solution = Solution()
# print(solution.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# print(solution.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(solution.findItinerary(tickets = [["JFK","ATL"],["ATL","JFK"]]))
# print(solution.findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# print(solution.findItinerary(tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
print(solution.findItinerary(tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))


# ans is 21 itinerary elements
