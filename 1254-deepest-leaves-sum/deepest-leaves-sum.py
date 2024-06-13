# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        a=deque()
        s=[0,0]
        a.append((root,0))
        while a:
            b,l=a.popleft()
            if not b.left and not b.right and s[1]==l:
                s[0]+=b.val
            else:
                if b.left:
                    a.append((b.left,l+1))
                    s=[0,l+1]
                if b.right:
                    a.append((b.right,l+1))
                    s=[0,l+1]
        return s[0]