from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
                last_non_zero += 1

l = [0,1,2,3,4,0,6,0,8,9]
Solution().moveZeroes(l)
print(l)


