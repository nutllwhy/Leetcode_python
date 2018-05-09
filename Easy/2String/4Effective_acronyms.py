# 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
# 说明:
# 你可以假设字符串只包含小写字母。

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # ranking 54%:转换成列表，然后排序，比较两个排序后的列表是否相同
        if len(s) != len(t):
        	return False
        else:
        	s1 = list(s)
        	t1 = list(t)
        	s1.sort()
        	t1.sort()
        	return s1 == t1