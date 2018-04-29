# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 解题思路：这题乍一看很简单，最末尾+1就行，其实题目具有迷惑性，没有告诉你进位的情况，要自己去分析
# 用一个指针标记最末尾，如果最末尾不是9，直接+1
# 如果是9，这位变成0，指针往前一位，再次判断是不是9
# 还要考虑，99->100这样数组需要多一位数字的情况，inset加一位数字在开头

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        while (digits[index] == 9) and (index != 0):
        	digits[index] = 0
        	index = index - 1
        if (digits[index] == 9) and (index == 0):
        	digits[index] = 0
        	digits.insert(0, 0)
        digits[index] = digits[index] + 1
        return digits
