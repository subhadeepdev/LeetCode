# from typing import str
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letterCount = collections.Counter(t)
        toContain = len(t)
        minLeft = -1
        minLength = len(s) + 1

        left = 0
        for right, char in enumerate(s):
            letterCount[char] -= 1
            if letterCount[char] >= 0:
                toContain -= 1
            
            while toContain == 0:
                if right - left + 1 < minLength:
                    minLeft = left
                    minLength = right - left + 1
                letterCount[s[left]] += 1
                if letterCount[s[left]] > 0:
                    toContain += 1
                left += 1
            
        return "" if minLeft == -1 else s[minLeft: minLeft + minLength]
                

solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))