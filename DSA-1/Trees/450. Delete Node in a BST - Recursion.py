# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMinNodeVal(root):
            while root and root.left:
                root = root.left
            return root.val

        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                minNodeVal = findMinNodeVal(root.right)
                root.val = minNodeVal
                root.right = self.deleteNode(root.right, minNodeVal)
        return root
        