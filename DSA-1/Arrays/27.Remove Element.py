# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l= 0
        n= len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l