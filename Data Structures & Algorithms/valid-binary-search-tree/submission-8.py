# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr,leftm,rightm):
            if not curr:
                return True
            
            if not curr.val<rightm or not curr.val>leftm:
                return False
            
            return dfs(curr.left,leftm,curr.val) and dfs(curr.right,curr.val,rightm)
        
        return dfs(root,float("-inf"),float("inf"))