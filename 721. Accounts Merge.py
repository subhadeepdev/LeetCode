from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parents = list(range(size))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dataStructure = UnionFind(len(accounts))
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    dataStructure.union(i, ownership[email])
                ownership[email] = i

        answer = defaultdict(list)
        for email, owner in ownership.items():
            answer[dataStructure.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in answer.items()]
    
solution = Solution()
print(solution.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))