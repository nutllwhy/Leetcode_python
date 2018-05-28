# 给定一个二叉树，返回其按层次遍历的节点值。（即逐层地，从左到右访问所有节点）

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
        	return res

        q = []
        # 一个临时栈，每一层的左右孩子都保存在临时栈中
        q.append(root)
        # 头结点入栈
        while len(q) != 0:
        	tmp = []
        	for i in range(len(q)):
        		# 层级遍历
        		r = q.pop(0)
        		# 头结点出栈，左右孩子入栈
        		if r.left:
        			q.append(r.left)
        		if r.right:
        			q.append(r.right)
        		tmp.append(r.val)
        		# 保存头结点的值
        	res.append(tmp)

        return res


