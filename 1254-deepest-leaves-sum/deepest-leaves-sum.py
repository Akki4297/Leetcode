# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        a=[]
        b=[]
        c=[]
        s=0
        a.append(root)
        if not a[0].left and not a[0].right:
            return a[0].val
        while a != []:
            c=b.copy()
            b=[]
            for _ in a:
                if _.left :
                    b.append(_.left)
                if _.right:
                    b.append(_.right)
            a=b.copy()
        for _ in c:
            s += _.val
        return s

