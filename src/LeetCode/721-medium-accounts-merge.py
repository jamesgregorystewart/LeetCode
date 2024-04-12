"""
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

johnsmith: john, john_newyork, john00@mail.com
john_newyork: john, johnsmith, john_newyork
mary@mail.com: mary
johnnybravo: john

john: johnsmith, john_newyork, john00@mail.com
johnsmith johnnewyork

johnsmith: john

{'David0@m.co': 'David0@m.co', 
'David1@m.co': 'David0@m.co',
'David3@m.co': 'David0@m.co', 
'David4@m.co': 'David3@m.co',
'David5@m.co': 'David3@m.co', 
'David2@m.co': 'David3@m.co'}
"""

from typing import List
from collections import defaultdict

"""
Number of accounts will be the count of keys after counting the values in uf.root
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        for account in accounts:
            name = account[0]
            if len(account) < 2:
                continue
            if len(account) == 2:
                uf.find(account[1])
            for i in range(1, len(account) - 1):
                uf.union(account[i], account[i + 1])
                uf.map_user(account[i], name)
            uf.map_user(account[-1], name)

        aliases = defaultdict(list)
        for email in uf.root:
            root = uf.find(email)
            aliases[root].append(email)

        ans = []
        for key, emails in aliases.items():
            account = [uf.emails_to_name[key]] + sorted(emails)
            ans.append(account)
        return ans


class UnionFind:
    def __init__(self) -> None:
        self.root = {}
        self.rank = {}
        self.emails_to_name = {}

    def find(self, x) -> str:
        if x not in self.root:
            self.root[x] = x
            self.rank[x] = 0
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def map_user(self, email, name):
        self.emails_to_name[email] = name
