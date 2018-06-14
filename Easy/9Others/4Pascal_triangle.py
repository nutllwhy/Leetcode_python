# 帕斯卡三角形
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # https://blog.csdn.net/coder_orz/article/details/51589254
        # 方法一：从第二行开始，每一行数据都是新生成的
        if numRows == 0:
        	return []
        res = [[1]]
        for i in range(1, numRows):
        	# 加一行
        	res.append([])
        	for j in range(i+1):
        		# j>0控制左边，j<i控制右边
        		res[i].append((res[i-1][j-1] if j > 0 else 0) + (res[i-1][j] if j < i else 0))
        return res

        # 方法二：因为每一行的头尾都是1，可以节省一部分计算量
        # 按行数每行都预设都1，再修改中间的数字
        res = []
        for i in range(0, numRows):
        	res.append([1] * (i+1))
        	for j in range(1, i):
        		res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res