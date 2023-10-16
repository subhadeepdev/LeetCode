from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        numsLeft, numsRight, output = [], [], []

        sum = 1
        numsLeft.append(sum)
        for num in nums:
            sum *= num
            numsLeft.append(sum)
        numsLeft.append(1)

        sum = 1
        numsRight.append(sum)
        for num in reversed(nums):
            sum *= num
            numsRight.append(sum)
        numsRight.append(1)
        numsRight.reverse()

        for i in range(0, len(nums)):
            output.append(numsLeft[i - 1] * numsRight[i + 1])

        return output



sln = Solution()
print(sln.productExceptSelf([1,2,3,4]))
        