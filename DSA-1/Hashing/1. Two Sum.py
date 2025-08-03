class Solution:

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def twoSumSorting(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = list(enumerate(nums))
        indexed_nums.sort(key=lambda x: x[1])
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][1] + indexed_nums[right][1]
            if current_sum == target:
                return [indexed_nums[left][0], indexed_nums[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
    
    def twoSumTwoPass(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        
        for i, num in enumerate(nums):
            indices[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
        return []
    
    def twoSumOnePass(self, nums: List[int], target: int) -> List[int]:
        indices = {}                
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices:
                return [indices[diff], i]
            indices[num] = i
        return []
    