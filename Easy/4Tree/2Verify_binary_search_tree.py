# 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #方法一：不递归
        sta = []
        res = []
        t = root
        while t or sta:
            while t:
                sta.append(t)
                t = t.left
            t = sta.pop()
            res.append(t.val)
            t = t.right
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
        # 方法二：递归
        if root == None or root.left == None or root.right == None:
        	return True

        if root.left:
        	if not self.isValidBST(root.left):
        		return False
        	elif self.max_val(root.left) >= root.val:
        		return False

        if root.right:
        	if not self.isValidBST(root.right):
        		return False
        	elif self.min_val(root.right) <= root.val:
        		return False

        return True

    def min_val(self, root):
    	result = root.val
    	while root.left:
    		result = root.left.val
    		root = root.left
    	return result

    def max_val(self, root):
    	result = root.val
    	while root.right:
    		result = root.right.val
    		root = root.right
    	return result