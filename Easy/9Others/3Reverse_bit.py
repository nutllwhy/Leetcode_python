# 颠倒二进制位
# 颠倒给定的 32 位无符号整数的二进制位

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	# 十进制转二进制，切片
    	s = bin(n)[2:]
    	# 补全0
    	s = '0' * (32-len(s)) + s
    	s = s[::-1]
    	# 二进制转十进制
    	return int(s,2)