# 字谜分组
# 给定一个字符串数组，将字母异位词组合在一起。
# 字母异位词指字母相同，但排列不同的字符串。

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 字典，key为每一个单词排序后的字符串
        # https://juejin.im/pin/5ad07aa5092dcb5883283ffc
        bucket = {}
        for ele in strs:
            key = "".join(sorted(ele))
            if key not in bucket.keys():
                bucket[key] = [ele]
            else:
                bucket[key].append(ele)
        strs_new = [value for value in bucket.values()]
        return strs_new
