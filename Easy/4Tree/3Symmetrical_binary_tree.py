# 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
        	return True
        if root.left == None and root.right == None:
        	return True
        if (root.left and not root.right) or (root.right and not root.left):
            return False
        
        def is_same(p1, p2):
        	if not p1 and not p2:
        		return True
        	if (p1 and p2) and p1.val == p2.val:
        		return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
        	return False

        return is_same(root.left, root.right)
