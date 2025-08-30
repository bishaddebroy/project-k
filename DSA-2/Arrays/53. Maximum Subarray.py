class Solution:
    # Brute Force. Time: O(n^3) Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                maxSum = max(maxSum, sum(nums[i:j+1]))

        return maxSum

    # Brute Force. Time: O(n^2) Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)

        return maxSum

    # Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)

        return maxSum