from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i, row in enumerate(grid):
            for j, cell in enumerate(grid[i]):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    grid[i][j] = 0

        dirs = [0, 1, 0, -1]
        time = -1 if queue else 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k in range(len(dirs)):
                    new_i = i + dirs[k - 1]
                    new_j = j + dirs[k]
                    if 0 <= new_i and new_i < len(grid) and \
                        0 <= new_j and new_j < len(grid[0]) and \
                        grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 0
                        queue.append((new_i, new_j))
            time += 1

        for i, row in enumerate(grid):
            for j, cell in enumerate(grid[i]):
                if grid[i][j] == 1:
                    return -1
        return time

sol = Solution()
print(sol.orangesRotting([[1],[2],[1],[2]]))
