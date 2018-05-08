# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。
# 如果不存在，则返回 -1。

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 大笨蛋超时做法
        # flag = -1
        # i = 0
        # while i < len(s):
        # 	if s.count(s[i]) == 1:
        # 		flag = i
        # 		break
        # 	else:
        # 		i = i + 1
        # return flag

        # 建立哈希表
        # 字符长度为8的数据类型共有265种可能
        ls = [0]*256
        # 遍历字符串，key为ASCII值，值为该字母出现的次数
        for i in s:
        	ls[ord(i)] += 1
        # 遍历列表，找到第一个值为1的字母，输出其位置
        for j in s:
        	if ls[ord(j)] == 1:
        		return s.index(j)
        		break
        return -1

