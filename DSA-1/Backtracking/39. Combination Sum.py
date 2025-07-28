class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curSum, subset):
            if i >= len(candidates) or curSum > target:
                return
            
            if curSum == target:
                res.append(subset.copy())
                return

            subset.append(candidates[i])
            dfs(i, curSum + candidates[i], subset)

            subset.pop()
            dfs(i+1, curSum, subset)
        
        dfs(0, 0, [])
        return res