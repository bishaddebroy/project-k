class Solution:
    # Brute Force. Time Complexity: O(N^2), Space Complexity: O(1).
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            for R in range(L + 1, min(L + k + 1, len(nums))):
                if nums[L] == nums[R]:
                    return True
        return False

    # Hash Map. Time Complexity: O(N), Space Complexity: O(N).
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        
        return False

    # Sliding Window. Time Complexity: O(N), Space Complexity: O(K).
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        
        return False