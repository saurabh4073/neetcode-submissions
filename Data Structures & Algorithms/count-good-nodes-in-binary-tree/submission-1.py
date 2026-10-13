# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(curr, maxi):
            if not curr:
                return 0
            
            if curr.val>=maxi:
                res.append(curr.val)
            maxi=max(maxi,curr.val)
            dfs(curr.left, maxi)
            dfs(curr.right,maxi)

        dfs(root,root.val)
        return len(res)