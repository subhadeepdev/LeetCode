from typing import List
import bisect

class Solution:
    def findBreak(self, nums):
        leftVal, rightVal = nums[0], nums[-1]
        leftIndex, rightIndex = 0, len(nums) - 1
        while leftIndex < rightIndex:
            midIndex = (leftIndex + rightIndex) // 2
            if leftVal <= nums[midIndex]:
                if leftIndex == midIndex:
                    return rightIndex
                leftIndex = midIndex
            elif nums[midIndex] <= rightVal:
                rightIndex = midIndex
        return leftIndex
    
    def search(self, nums: List[int], target: int) -> int:
        breakPoint = self.findBreak(nums)
        # print(breakPoint)
        if nums[0] <= target:
            index = bisect.bisect_left(nums, target, 0, breakPoint)
        else:
            index = bisect.bisect_left(nums, target, breakPoint)
        if index < len(nums) and nums[index] == target:
            return index
        return -1

        

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))