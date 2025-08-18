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
    
    # Bidirectional BFS approach
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0],
                    [1, 1], [1, -1], [-1, 1], [-1, -1]]

        if grid[0][0] or grid[R - 1][C - 1]:
            return -1
        if R == 1 and C == 1:  # Single cell case
            return 1

        def bidirectional_bfs():
            start_q = collections.deque([(0, 0)])
            end_q = collections.deque([(R - 1, C - 1)])
            
            start_visit = {(0, 0)}
            end_visit = {(R - 1, C - 1)}

            length = 2
            
            while start_q and end_q:
                for _ in range(len(start_q)):
                    r, c = start_q.popleft()
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0 or nr == R or nc == C
                            or (nr, nc) in start_visit or grid[nr][nc] == 1):
                            continue
                        
                        if (nr, nc) in end_visit:
                            return length  # Found meeting point!
                        
                        start_q.append((nr, nc))
                        start_visit.add((nr, nc))
                
                for _ in range(len(end_q)):
                    r, c = end_q.popleft()
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0 or nr == R or nc == C
                            or (nr, nc) in end_visit or grid[nr][nc] == 1):
                            continue
                        
                        if (nr, nc) in start_visit:
                            return length + 1  # Found meeting point! (+1 for end step)
                        
                        end_q.append((nr, nc))
                        end_visit.add((nr, nc))
                
                length += 2
            
            return -1

        return bidirectional_bfs()