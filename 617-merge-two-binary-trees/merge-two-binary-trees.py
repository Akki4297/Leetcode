# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)
        
        return root1
        '''if not root1 and root2:
            return root2
        def merge(root1,root2):
            if root1 and root2:
                root1.val = root1.val + root2.val
                if root1.left or root2.left:
                    if not root1.left and root2.left:
                        root1.left = root2.left
                    else:
                        merge(root1.left,root2.left)
                if root1.right or root2.right:
                    if not root1.right and root2.right:
                        root1.right = root2.right
                    else:
                        merge(root1.right,root2.right)
            return
        merge(root1,root2)
        return root1'''