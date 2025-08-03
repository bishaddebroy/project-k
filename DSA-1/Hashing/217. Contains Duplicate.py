class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def containsDuplicateBruteForce(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    # Time Complexity: O(n log n)
    # Space Complexity: O(1) if we ignore the space used by sorting
    def containsDuplicateSorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def containsDuplicateHashSet(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
