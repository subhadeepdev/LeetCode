from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        outputList = []

        def dfs(target, start, combination):
            if target < 0:
                return
            if target == 0:
                outputList.append(combination.copy())
                return
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                dfs(target - candidates[i], i, combination)
                combination.pop()

        candidates.sort()
        dfs(target, 0, [])
        return outputList

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))