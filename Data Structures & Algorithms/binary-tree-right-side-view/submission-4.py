# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q= deque([root])

        while q:
            qlen = len(q)
            rightnode = None
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightnode=node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightnode:
                res.append(rightnode)
        return res
