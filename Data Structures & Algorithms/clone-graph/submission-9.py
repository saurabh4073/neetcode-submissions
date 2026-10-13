"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldtonew={}
        def clone(node):
            if node in oldtonew:
                return oldtonew[node]
            
            oldtonew[node]=Node(node.val)
            for nei in node.neighbors:
                oldtonew[node].neighbors.append(clone(nei))
            
            return oldtonew[node]
        return clone(node)