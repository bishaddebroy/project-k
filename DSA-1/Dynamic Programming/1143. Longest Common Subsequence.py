class Solution:
    # brute force DFS - exponential time complexity O(2^(m+n)) and O(m+n) space complexity
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            else:
                return max(dfs(i+1, j), dfs(i, j+1))

        return dfs(0, 0)
    
    # DFS with memoization (Top-Down DP) - O(m*n) time and space complexity
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[(i, j)]

        return dfs(0, 0)
    
    # Dynamic Programming (Tabulation) (Bottom-Up DP) - O(m*n) time and space complexity
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
            
        return dp[0][0]
    
    # Dynamic Programming with optimized space - O(m*n) time and O(min(m,n)) space complexity
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(curr[j+1], prev[j])
            prev, curr = curr, prev # swap references, so prev always has the last computed row
            
        return prev[0]
    
    # Dynamic Programming with further optimized space - O(m*n) time and O(min(m,n)) space complexity
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev_diagonal = 0
            for j in range(len(text2) - 1, -1, -1):
                tmp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev_diagonal
                else:
                    dp[j] = max(dp[j+1], dp[j])
                prev_diagonal = tmp
        return dp[0]
    