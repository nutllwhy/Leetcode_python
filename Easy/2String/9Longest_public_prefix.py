# 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 说明：所有输入只包含小写字母 a-z 。

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 不排序做法60ms：第一个的每一位和后面的每一位对比
        if strs is None or len(strs) == 0:
        	return ''
        res = strs[0]
        for i in range(1,len(strs)):
        	temp = res
        	res = ''
        	for j in range(min(len(strs[i]), len(temp))):
        		if temp[j] == strs[i][j]:
        			res = res + temp[j]
        		else:
        			break
        return res
        
        # 排序做法48ms：排完之后比较第一个和最后一个公共前缀
        if not strs:
            return ''
        strs.sort()
        res = ''
        for i in range(len(strs[0])):
            if strs[-1][i] != strs[0][i]:
                return res
            res += strs[0][i]
        return res
