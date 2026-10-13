# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=[]
        
        def dfs(curr,maxval):
            if not curr:
                return 0
            
            if curr.val>=maxval:
                res.append(curr.val)
            maxval= max(maxval,curr.val)
            dfs(curr.left,maxval)
            dfs(curr.right,maxval)
        
        dfs(root,root.val)
        return len(res)
