class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.c=0
        def sum(root,s,f):
            if not root:
                return [0,0]
            s1,f1 = sum(root.left,s,f)
            s2,f2 = sum(root.right,s,f)
            s = s1+s2+root.val 
            f = f1+f2+1
            if root.val == (s//f):
                self.c+=1
            return [s,f]
        s,f = sum(root,0,0)
        return self.c