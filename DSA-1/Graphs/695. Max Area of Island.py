class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == R or c == C or
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            visit.add((r, c))
            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        area = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r, c))
        
        return area

    # Iterative BFS.
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visit.add((r, c))
            area = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr == R or nc == C or
                        grid[nr][nc] == 0 or (nr, nc) in visit):
                        continue

                    queue.append((nr, nc))
                    visit.add((nr, nc))
                    area += 1
            
            return area

        area = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, bfs(r, c))
        
        return area
    