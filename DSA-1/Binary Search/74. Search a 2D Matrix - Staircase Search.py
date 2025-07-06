class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        r, c = 0, COL - 1

        while r < ROW and c >= 0:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                return True
        
        return False
# Time Complexity: O(ROW + COL)
# Space Complexity: O(1)