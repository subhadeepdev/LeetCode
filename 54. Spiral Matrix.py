from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return ""
        row_s, row_e = 0, len(matrix) - 1
        colm_s, colm_e = 0, len(matrix[0]) - 1
        spiral = []
        while row_s < row_e and colm_s < colm_e:
            i = row_s
            for j in range(colm_s, colm_e):
                spiral.append(matrix[i][j])
            j = colm_e
            for i in range(row_s, row_e):
                spiral.append(matrix[i][j])
            i = row_e
            for j in range(colm_e, colm_s, -1):
                spiral.append(matrix[i][j])
            j = colm_s
            for i in range(row_e, row_s, -1):
                spiral.append(matrix[i][j])
            row_s += 1
            row_e -= 1
            colm_s += 1
            colm_e -= 1
        if row_s == row_e and colm_s == colm_e:
            spiral.append(matrix[row_s][colm_s])
        elif colm_s == colm_e:
            j = colm_s
            for i in range(row_s, row_e + 1):
                spiral.append(matrix[i][j])
        elif row_s == row_e:
            i = row_s
            for j in range(colm_s, colm_e + 1):
                spiral.append(matrix[i][j])
        return spiral


print(Solution().spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]))
# [1,2,3,4,5,6,7,8,9,10,20,19,18,17,16,15,14,13,12,11]