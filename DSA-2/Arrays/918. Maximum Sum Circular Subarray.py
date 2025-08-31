class Solution:
    # Brute Force. Time: O(n^2) Space: O(1)
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        for i in range(n):
            curSum = 0
            for j in range(i, i + n):
                curSum += nums[j % n]
                res = max(res, curSum)
        
        return res

    # Kadane's Algorithm
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
        
        return max(globMax, total - globMin) if globMax > 0 else globMax