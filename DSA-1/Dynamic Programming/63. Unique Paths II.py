class Solution:
    # DFS with memoization (Top-Down DP) - O(m*n) time and space complexity
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        cache = {(R-1, C-1): 1}

        def dfs(r, c):
            if r == R or c == C or obstacleGrid[r][c]:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]

        return dfs(0, 0)
    
    # Dynamic Programming (Tabulation) (Bottom-Up DP) - O(m*n) time and space complexity
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[R-1][C-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        dp[R-1][C-1] = 1

        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
    
    # Dynamic Programming with optimized space - O(m*n) time and O(n) space complexity
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[R-1][C-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        row = [0] * (C + 1)
        row[C-1] = 1

        for r in range(R-1, -1, -1):
            newRow = [0] * (C + 1)
            for c in range(C-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    newRow[c] = 0
                else:
                    newRow[c] = newRow[c + 1] + row[c]
            row = newRow
        
        return row[0]
    
    # Same as above but with only one row array
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[R-1][C-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        row = [0] * C
        row[C-1] = 1

        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    row[c] = 0
                elif c < C - 1:
                    row[c] = row[c] + row[c + 1] # or row[c] += row[c + 1]
        
        return row[0]
    
    # Modifying the input grid to save space - O(m*n) time and O(1) space complexity
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[R-1][C-1] == 1:
            return 0
        
        obstacleGrid[R-1][C-1] = 1

        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if r == R-1 and c == C-1:
                    continue

                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    down = obstacleGrid[r+1][c] if r+1 < R else 0
                    right = obstacleGrid[r][c+1] if c+1 < C else 0
                    obstacleGrid[r][c] = down + right
        
        return obstacleGrid[0][0]
        