class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) -1

        while l <= r:
            mid = l + (r - l) // 2
            # mid = (l + r) // 2  # This can cause overflow in some languages, but not in Python

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
        