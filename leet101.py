# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def mirror(root):
            if not root:
                return
            temp = root.right
            root.right = root.left
            root.left = temp
            mirror(root.right)
            mirror(root.left)

        val_1 = []
        val_2 = []

        def preTraverse1(root):
            if not root:
                val_1.append(-1)
                return
            val_1.append(root.val)
            preTraverse1(root.left)
            preTraverse1(root.right)

        def preTraverse2(root):
            if not root:
                val_2.append(-1)
                return
            val_2.append(root.val)
            preTraverse2(root.left)
            preTraverse2(root.right)

        preTraverse1(root.left)

        mirror(root.right)
        preTraverse2(root.right)
        # print(val_1,val_2)
        return val_1 == val_2
