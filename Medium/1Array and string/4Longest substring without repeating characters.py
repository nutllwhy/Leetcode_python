# 无重复字符的最长子串
# 给定一个字符串，找出不含有重复字符的最长子串的长度。

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 错误解法：对字符串“dvdf”等最长序列出现在后方的字符串无效
        # if len(s) == 0:
        #     return 0
        # bucket = {}
        # l = list(s)
        # key = 0
        # max_len = 0
        # bucket[key] = l[0]
        # for ele in l[1:]:
        #     if ele not in bucket[key]:
        #         bucket[key] += ele
        #     else:
        #     	key += 1
        #     	bucket[key] = ele
        # for key in bucket.keys():
        # 	if len(bucket[key]) > max_len:
        # 		max_len = len(bucket[key])
        # return max_len

        # https://blog.csdn.net/yurenguowang/article/details/77839381
        res = 0
        if s is None or len(s) == 0:
            return res
        d = {}
        tmp = 0  
        start = 0  # 记录截取字符串的开始位置
        for i in range(len(s)):
            # 出现和start位置相同的元素之后，start+1（截断开始处后移一位）
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            tmp = i - start + 1   # 当前循环字母到start位置的长度
            d[s[i]] = i  # 更新该字母最新位置
            res = max(res, tmp)
        return res