# 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。
# 请使用原地算法。

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # row_0, col_0表示第一行，第一列是否为0
        row_0, col_0 = False, False
        n = len(matrix)
        m = len(matrix[0])
        # 检查第一行所有元素是否存在0
        for i in range(n):
            if matrix[i][0] == 0:
                col_0 = True
                break
        # 检查第一列所有元素是否存在0
        for j in range(m):
            if matrix[0][j] == 0:
                row_0 = True
                break
        # 扫描其余元素，并在第一行，第一列记录
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0 
        # 按照第一行，第一列的记录，修改矩阵中其余元素
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(1,m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0 
        # 修改第一行，第一列
        if row_0 == True:
            for j in range(m):
                matrix[0][j] = 0 
        if col_0 == True:
            for i in range(n):
                matrix[i][0] = 0
