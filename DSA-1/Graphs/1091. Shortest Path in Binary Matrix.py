class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0],
                    [1, 1], [1, -1], [-1, 1], [-1, -1]]

        def bfs(r, c):
            q = collections.deque()
            visit = set()
            q.append((r, c))
            visit.add((r, c))

            length = 1
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if r == R - 1 and c == C - 1:
                        return length
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0 or nr == R or nc == C
                            or (nr, nc) in visit or grid[nr][nc] == 1):
                            continue
                        q.append((nr, nc))
                        visit.add((nr, nc))
                length += 1
            return -1
                
        return bfs(0, 0) if not grid[0][0] and not grid[R - 1][C - 1] else -1