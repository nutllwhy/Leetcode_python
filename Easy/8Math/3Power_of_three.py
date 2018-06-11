# 3的幂
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
# 
# class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 方法一：用循环
        if n == 0:
        	return False
        if n == 1:
            return True
        while n % 3 == 0:
        	n = n / 3
        	if n == 1:
        		return True
        return False

        # 方法二：3^19是int范围内最大的3的幂
        # 那么3^19可以被任何3的幂整除
        return n > 0 and 1162261467 % n == 0