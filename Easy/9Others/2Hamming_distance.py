# 汉明距离
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 给出两个整数 x 和 y，计算它们之间的汉明距离。

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 老实人做法
        count = 0
        s = bin(x ^ y)
        for i in range(2,len(s)):
        	if s[i] == '1':
        		count += 1
        return count

        # 一行
        return bin(x^y).count('1')
