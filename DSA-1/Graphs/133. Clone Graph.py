"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # visit set will not work here as we need to create new nodes and map them to old nodes for tracking cloning

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            if not node:
                return node
                
            new = Node(node.val)
            oldToNew[node] = new
            for neighbor in node.neighbors:
                new.neighbors.append(dfs(neighbor))
            return new

        return dfs(node)