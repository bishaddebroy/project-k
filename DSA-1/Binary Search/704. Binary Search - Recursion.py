class Solution:
    # Way 1
    def binary_serach(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binary_serach(mid + 1, r, nums, target)
        return self.binary_serach(l, mid -1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_serach(0, len(nums) - 1, nums, target)
        

    # Way 2
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            if l > r:
                return -1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, r)
            else:
                return binary_search(l, mid - 1)

        return binary_search(0, len(nums) - 1)