from typing import List
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @cache
        def wordBreak(s):
            if s in wordSet:
                return True
            return any(s[:i] in wordSet and wordBreak(s[:i]) for i in range(len(s)))
        
        return wordBreak(s)

solution = Solution()
print(solution.wordBreak("leetcode", ["leet","code"]))
