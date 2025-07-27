class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            dfs(i + 1)
            subset.append(nums[i])

            dfs(i + 1)
            subset.pop()
        
        dfs(0)
        return res
    
    def subsetsIterative(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
    
    
    