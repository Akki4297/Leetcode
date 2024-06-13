# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.c=0
        def sum(root,s,f):
            if not root.left and not root.right :
                print(s,f)
                return [root.val,1]
            else:
                s1,s2,f1,f2=0,0,0,0
                if root.left:
                    s1,f1 = sum(root.left,s,f)
                    if root.left.val == (s1//f1):
                        self.c+=1
                if root.right:
                    s2,f2 = sum(root.right,s,f)
                    if root.right.val == (s2//f2):
                        self.c+=1
                print(s1,s2,f1,f2,s1+s2+root.val,f1+f2+1)
            return [s1+s2+root.val,f1+f2+1]
        s,f = sum(root,0,0)
        print(s,f)
        if root.val == s//f:
            self.c+=1
        return self.c
