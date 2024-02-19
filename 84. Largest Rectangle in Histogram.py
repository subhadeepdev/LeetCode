from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxRight = [n - i - 1 for i in range(n)]
        i = 0
        for j in range(len(heights)):
            if heights[i] > heights[j]:
                maxRight[i] = j - i - 1
                i += 1

        maxLeft = [i for i in range(n)]
        i = len(heights) - 1
        for j in range(len(heights) - 1, -1, -1):
            if heights[i] > heights[j]:
                maxLeft[i] = i - j - 1
                i -= 1

        return max(heights[i] * (1 + maxLeft[i] + maxRight[i]) for i in range(len(heights)))
    
print(Solution().largestRectangleArea([2,1,5,6,2,3]))