# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def inorder(root):
            nonlocal cnt, res
            if not root:
                return
            inorder(root.left)
            cnt -= 1
            if cnt == 0:
                res = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return res
    
    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

    def kthSmallestMorris(self, root: Optional[TreeNode], k: int) -> int:
        cur = root

        while cur:
            if not cur.left:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            else:
                ip = cur.left
                while ip.right and ip.right != cur:
                    ip = ip.right

                if not ip.right:
                    ip.right = cur
                    cur = cur.left
                else:
                    ip.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right