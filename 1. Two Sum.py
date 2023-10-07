class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsEnum = list(enumerate(nums))
        numsEnum.sort(key = lambda x: x[1])
        i, j = 0, len(numsEnum) - 1
        while i < j:
            currSum = numsEnum[i][1] + numsEnum[j][1]
            if currSum == target:
                return [numsEnum[i][0], numsEnum[j][0]]
            if currSum < target:
                i += 1
            else:
                j -= 1
        return None        