# 罗马数字转整数
# 罗马数字包含以下七种字符：I， V， X， L，C，D 和 M。
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。
# 但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 从后往前遍历字符串s
        # 因为最后一项没有后一项，除外
        # 如果当前项的值小于后一项，则做减法，反之加法
        count = 0
        if len(s) == 0:
        	return count
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)-1, -1, -1):
        	if i != len(s) - 1:
        		if dic[s[i]] < dic[s[i+1]]:
        			count -= dic[s[i]]
        		else:
        			count += dic[s[i]]
        	else:
        		count +=dic[s[i]]
        return count
