from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outputList = []
        usedList = [False] * len(nums)

        def dfs(permutation: List[int]) -> None:
            if len(permutation) == len(nums):
                outputList.append(permutation.copy())
                return
            for i, num in enumerate(nums):
                if usedList[i]:
                    continue
                permutation.append(num)
                usedList[i] = True
                dfs(permutation)
                permutation.pop()
                usedList[i] = False
            return
        
        dfs([])
        return outputList
    
sol = Solution()
print(sol.permute([1,2,3]))

        