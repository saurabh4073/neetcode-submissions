# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(curr, maxVal):
            if not curr:
                return 0
            
            if curr.val >=maxVal:
                res.append(curr.val)
            maxVal = max(maxVal,curr.val)
            dfs(curr.left,maxVal)
            dfs(curr.right,maxVal)
        
        dfs(root,root.val)
        return len(res)