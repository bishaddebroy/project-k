class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] >= target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        
        return l if (l < len(nums) and nums[l] == target) else -1
    
