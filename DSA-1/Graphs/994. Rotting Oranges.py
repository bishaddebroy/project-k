class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        time = 0
        fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < R and 0 <= nc < C and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1