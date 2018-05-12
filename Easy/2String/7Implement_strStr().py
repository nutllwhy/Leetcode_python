# 实现strStr()
# 实现 strStr() 函数。

# 给定一个 haystack 字符串和一个 needle 字符串，
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。

# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。
# 这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 自带find函数 48ms
        return haystack.find(needle)
        # 按逻辑解 80ms
        n = len(needle)
        if (n == 0) or (haystack == needle):
        	return 0
        else:
        	i = 0
        	flag = -1
        	while (i < len(haystack)) and (flag == -1):
        		if haystack[i:n+i] == needle:
        			flag = i
        		i = i + 1
        	return flag