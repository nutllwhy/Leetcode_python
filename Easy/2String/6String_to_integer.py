# 字符串转整数（atoi）
# 实现 atoi，将字符串转为整数。

# 在找到第一个非空字符之前，需要移除掉字符串中的空格字符。
# 如果第一个非空字符是正号或负号，选取该符号，
# 并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。
# 如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

# 字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。
# 当字符串中的第一个非空字符序列不是个有效的整数；
# 或字符串为空；或字符串仅包含空白字符时，则不进行转换。
# 若函数不能执行有效的转换，返回 0。

# 说明：
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
# 如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 解题思路：
        # 1. 先去掉开头所有空格
        # 2. 如果str[0]是正负号，就按照正负标记
        # 3. 对接下来的字符串进行判断：是否是数字，是的话加入num
        # 4. ord()求的是ASCLL码
        # 5. 最后判断是否越界
        str = str.strip()
        if not str:
            return 0
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >= '0' and c <= '9':
                number = 10*number + ord(c) - ord('0')
            else:
                break
        number = flag * number
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number
