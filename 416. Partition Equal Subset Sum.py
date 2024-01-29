from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ & 1:
            return False
        halfSum = sum_ // 2
        dpMatrix = [[False] * (halfSum + 1) for _ in range(len(nums) + 1)]

        dpMatrix[0][0] = True
        for sum_ in range(halfSum + 1):
            for i in range(1, len(nums) + 1):
                dpMatrix[i][sum_] = dpMatrix[i - 1][sum_] or (dpMatrix[i - 1][sum_ - nums[i - 1]] if sum_ >= nums[i - 1] else False)
        return dpMatrix[len(nums)][halfSum]
    
solution = Solution()
print(solution.canPartition([1,2,3,5]))