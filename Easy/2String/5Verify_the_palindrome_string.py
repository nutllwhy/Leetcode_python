# 验证回文字符串

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 大笨蛋100%超时做法
        # flag = True
        # l = list(filter(str.isalnum, s))
        # while l[0] and l[-1]:
        # 	if l[0] == l[-1]:
        # 		del l[-1]
        # 		del l[0]
        # 	else:
        # 		flag = False
        # return flag

        # 翻转，比较翻转前后是否一致
        s = s.lower()
        l = list(filter(str.isalnum, s))
        a = list(reversed(l))
        if l == a:
        	return True
        else:
        	return False