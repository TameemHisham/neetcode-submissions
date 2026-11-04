# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.levelOrderRec(root,0, res)
        return res
    def levelOrderRec(self,root, level, res):
        if not root:
            return 
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.levelOrderRec(root.left, level+1, res)
        self.levelOrderRec(root.right, level+1, res)