# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(node,leftm,rightm):
            if not node:
                return True
            
            if not node.val>leftm or not node.val<rightm:
                return False
            
            return isvalid(node.left,leftm,node.val) and isvalid(node.right,node.val,rightm)
        
        return isvalid(root,float("-inf"),float("inf"))
