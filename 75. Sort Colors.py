from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = centre = 0
        right = len(nums) - 1
        while 0 <= left <= centre <= right < len(nums):
            match nums[centre]:
                case 0:
                    nums[left], nums[centre] = nums[centre], nums[left]
                    left += 1
                    centre += 1
                case 1:
                    centre += 1
                case 2:
                    nums[centre], nums[right] = nums[right], nums[centre]
                    right -= 1

input = [2,0,2,1,1,0]
solution = Solution()
solution.sortColors(input)
print(input)
