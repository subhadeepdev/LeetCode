from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        outputIntervals = []
        outputInterval = intervals[0]
        for interval in intervals:
            if interval[0] <= outputInterval[1]:
                outputInterval[1] = max(outputInterval[1], interval[1])
            else:
                outputIntervals.append(outputInterval)
                outputInterval = interval
        if not outputIntervals or outputIntervals[-1] != outputInterval:
            outputIntervals.append(outputInterval)
        return outputIntervals

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))