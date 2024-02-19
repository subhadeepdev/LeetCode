from typing import List
import functools
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [[s, e, p] for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key = lambda x: x[1])
        
        @functools.cache
        def dp(i: int) -> int:
            if not i:
                return jobs[i][2]
            j = bisect.bisect_right(jobs, jobs[i][0], key = lambda x: x[1])
            if not j:
                return max(jobs[i][2], dp(i - 1))
            return max(jobs[i][2] + dp(j - 1), dp(i - 1))
            

        return dp(len(jobs) - 1)

print(Solution().jobScheduling([1,1,1], [2,3,4], [5,6,4]))