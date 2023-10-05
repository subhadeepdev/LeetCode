from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        maxLeft = [0]
        for currHeight in height:
            maxLeft.append(max(maxLeft[-1], currHeight))
        maxRight = [0]
        for currHeight in reversed(height):
            maxRight.append(max(maxRight[-1], currHeight))
        maxRight.reverse()
        return sum([max(0, min(maxLeft[i], maxRight[i]) - height[i]) for i in range(len(height))])
    
soln = Solution()
print(soln.trap([4,2,0,3,2,5]))