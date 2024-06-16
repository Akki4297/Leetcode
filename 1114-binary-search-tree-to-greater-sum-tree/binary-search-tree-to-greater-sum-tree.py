# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dst(root):       
            if not root: return
            nonlocal s
            dst(root.right)
            s += root.val
            root.val = s
            dst(root.left)
        s=0
        dst(root)
        return root
                