# 位1的个数
# 编写一个函数，输入是一个无符号整数，
# 返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 参考：http://www.cnblogs.com/klchang/p/8017627.html
        MAX_INT = 4294967295
        # 按位与运算
        # 对整数的二进制表示的每一位与 1 求与，统计结果为非 0 的个数
        # 需要移位的次数至少为整数的二进制表示中，数字 1 所在的最高位的位次，不够高效
        count, bit = 0, 1
        while n and bit <= MAX_INT + 1:
        	if bit & n:
        		count += 1
        		n -= bit
        	# 左移1位
        	bit = bit << 1
        return count

        # 快速算法
        # 用整数 i 与这个整数减 1 的值 i - 1，按位求与
        # 如此可以消除整数的二进制表示中最低位的 1
        count = 0
        while n:
        	count += 1
        	n = n & (n-1)
        return count

        # 吴老师做法
        count = 0
        while n:
        	count += 1
        	n -= n & (-n)
        return count  

        # 不用与运算的做法（味精喵贡献）
        # 对2取余，再整除2
        count = 0
        while n > 0:
            count += n % 2
            n = n / 2 
        return count