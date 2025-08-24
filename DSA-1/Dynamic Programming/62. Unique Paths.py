class Solution:
    # brute force DFS - exponential time complexity O(2^(m+n)) and O(m+n) space complexity
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)


        return dfs(0, 0)

    # DFS with memoization (Top-Down DP) - O(m*n) time and space complexity
    class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[i][j]

        return dfs(0, 0)

    # Dynamic Programming (Tabulation) (Bottom-Up DP) - O(m*n) time and space complexity
    class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
    
    # Same as above but without extra padding, as we know the last row and last column will always be 1
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
    
    # Dynamic Programming with optimized space - O(m*n) time and O(n) space complexity
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-2, -1, -1): # or for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
    
        return row[0]
    
    # Same as above but modifying the same row array instead of creating a new one because we only need the current and next values
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-2, -1, -1): # or for i in range(m-1):
            for j in range(n-2, -1, -1):
                row[j] = row[j + 1] + row[j]
    
        return row[0]
    