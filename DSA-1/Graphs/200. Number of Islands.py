class Solution:
    # Recursive DFS.
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == "0"):
                return
            
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        
        return islands

    # Recursive DFS with directions array. More scalable for larger number of directions.    
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == "0"):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        
        return islands

    # Iterative DFS. Check r, c -> mark r, c visited -> and explore and take all neighbors of r, c.
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            stack = [(r, c)] # BFS: queue = collections.deque([(r, c)]) (First in, first out.)
            # DFS is possible too with deque and pop() from the end. Last in, first out.
            
            while stack: # BFS: while queue:
                r, c = stack.pop() # BFS: r, c = queue.popleft() (FIFO)
                if (r < 0 or c < 0 or
                    r >= ROWS or c >= COLS or
                    (r, c) in visit or grid[r][c] == "0"): # or invert condition and visit and loop inside
                    continue
            
                visit.add((r, c))
                for dr, dc in directions:
                    stack.append((r + dr, c + dc)) # BFS: queue.append((r + dr, c + dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        
        return islands
    
    # Iterative DFS. Mark r, c visited. Explore all neighbors -> check neighbors -> mark and take the valid neighbors.
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            stack = [(r, c)]
            visit.add((r, c))  # Mark the starting cell as visited
            
            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and
                        nr < ROWS and nc < COLS and
                        (nr, nc) not in visit and grid[nr][nc] == "1"): # or invert condition, continue, and visit and loop outside
                        visit.add((nr, nc))
                        stack.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        
        return islands
    
    # BFS. Like the previous iterative DFS, but using a queue to explore neighbors.
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visit.add((r, c))
            
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and
                        nr < ROWS and nc < COLS and
                        (nr, nc) not in visit and grid[nr][nc] == "1"):
                        visit.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
    