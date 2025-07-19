class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        
        if not self.root:
            self.root = newNode
            return
        
        current = self.root
        while current:
            if key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            elif key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            else:
                current.value = val
                return

    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return -1

    def getMin(self) -> int:
        current = self.root

        while current and current.left:
            current = current.left
        
        return current.value if current else -1


    def getMax(self) -> int:
        current = self.root

        while current and current.right:
            current = current.right
        
        return current.value if current else -1


    def remove(self, key: int) -> None:
        if not self.root:
            return
        
        current = self.root
        parent = None

        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        
        if not current:
            return
        
        if not current.left or not current.right:
            child = current.left if current.left else current.right
            
            if not parent:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child
        
        else:
            delNode = current
            par = None

            current = current.right
            while current.left:
                par = current
                current = current.left
            
            if par:
                par.left = current.right
                current.right = delNode.right
            current.left = delNode.left

            if not parent:
                self.root = current
            elif parent.left == delNode:
                parent.left = current
            else:
                parent.right = current
        
        return

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
    
    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
