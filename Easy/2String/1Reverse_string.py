# 反转字符串
# 请编写一个函数，其功能是将输入的字符串反转过来。

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 做法一：切片法
        return s[::-1]

        # 做法二：借用列表的reverse方法(稍微慢一些)
        l = list(s)
        l.reverse()
        return "".join(l)