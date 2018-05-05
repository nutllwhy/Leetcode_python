# 旋转图像
# 给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
# 说明：你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。
#       请不要使用另一个矩阵来旋转图像。

# 解题思路：先将数组按照正对角线对称，再将每一行的向量进行翻转

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):  
            for j in range(len(matrix[0])-i):  
                temp = matrix[i][j+i]  
                matrix[i][j+i] = matrix[j+i][i]  
                matrix[j+i][i] = temp  
          
        for i in range(len(matrix)):  
            matrix[i].reverse()