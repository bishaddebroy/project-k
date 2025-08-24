class Solution:
    # brute force DFS - exponential time complexity O(2^n) and O(n) space complexity
    def rob(self, nums: List[int]) -> int:

        def dfs(i):
            if i >= len(nums):
                return 0
            return max(dfs(i + 1), nums[i] + dfs(i + 2))

        return dfs(0)

    # DFS with memoization (Top-Down DP) - O(n) time and space complexity
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
                
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)

    # Dynamic Programming (Tabulation) (Bottom-Up DP) - O(n) time and space complexity
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]

    # Dynamic Programming with optimized space - O(n) time and O(1) space complexity
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        
        # rob1, rob2 = dp[i-2], dp[i-1] # [rob1, rob2, i, i+1, ...]
        for i in range(len(nums)):
            tmp = max(rob2, nums[i] + rob1)
            rob1 = rob2
            rob2 = tmp

        return rob2