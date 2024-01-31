from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = [[]]
        for num in nums:
            for i in range(len(powerSet)):
                powerSet.append(powerSet[i] + [num])
        return powerSet

print(Solution().subsets([1,2,3]))