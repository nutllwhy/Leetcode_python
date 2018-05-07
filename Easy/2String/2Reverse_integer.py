# 颠倒整数

# 给定一个 32 位有符号整数，将整数中的数字进行反转。
# 注意：假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
# 根据这个假设，如果反转后的整数溢出，则返回 0。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x>2**31:
        	return 0
        else:
        	l = list(str(x))
        	if l[0] == '-':
        		del l[0]
        		l.reverse()
        		l.insert(0,'-')
       		else:
        		l.reverse()
        		while l[0] == '0':
        			del l[0]

        	x = int("".join(l))
        	if (x < -2**31) or (x > 2**31 - 1):
        		return 0
        	else:
        		return x

