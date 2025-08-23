class Solution:
    # brute force DFS - exponential time complexity O(2^n) and O(n) space complexity
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2)


        return dfs(0)
    
    # DFS with memoization (Top-Down DP) - O(n) time and space complexity
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i):
            if i >= n:
                return i == n
            if i in cache:
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]


        return dfs(0)
    
    # Dynamic Programming (Tabulation) (Bottom-Up DP) - O(n) time and space complexity
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[0]
    
    # Dynamic Programming with optimized space - O(n) time and O(1) space complexity
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 2, -1, -1):
            tmp = one
            one = one + two
            two = tmp
        
        return one