# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curSum):
            if not node:
                return False
            
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum

            if dfs(node.left, curSum):
                return True
            if dfs(node.right, curSum):
                return True
            return False
            # alternative: return dfs(node.left, curSum) or dfs(node.right, curSum)
        
        return dfs(root, 0)
        
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum) or
                (not targetSum and not root.left and not root.right))
    
    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)]
        while stack:
            node, curSum = stack.pop()

            if not node.left and not node.right and curSum == 0:
                return True
            if node.right:
                stack.append((node.right, curSum - node.right.val))
            if node.left:
                stack.append((node.left, curSum - node.left.val))
        
        return False
            
    def hasPathSumBFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        q = collections.deque([(root, targetSum - root.val)])
        while q:
            node, curSum = q.popleft()

            if not node.left and not node.right and curSum == 0:
                return True
            if node.left:
                q.append((node.left, curSum - node.left.val))
            if node.right:
                q.append((node.right, curSum - node.right.val))
        
        return False
            
        