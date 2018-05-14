# 数数并说
# 报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

# 给定一个正整数 n ，输出报数序列的第 n 项。
# 注意：整数顺序将表示为一个字符串

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 耿直超时做法
        # start_str = "1"
        # while n > 1:
        #     chars = list(start_str)
        #     sb = []
        #     i = 0
        #     while i < len(chars):
        #         count = 0
        #         tmp = chars[i]
        #         while i < len(chars) and chars[i] == tmp:
        #             count = count + 1
        #             i = i + 1
        #         sb.append(str(count)+tmp)
        #     start_str = "".join(sb)
        # return start_str
        start_str = "1"
        for i in range(1,n):
        	start_str = self.myfun(start_str)
        return start_str

    def myfun(self,start_str):
    	res=""
    	dict={}
    	for s in start_str:
    		if len(dict) is 0:
    			dict[s]=1
    		else:
    			if s not in dict.keys():
    				name = list(dict.keys())[0]
    				count = dict[name]
    				res += str(count) + str(name)
    				del dict[name]
    				dict[s] = 1
    			else:
    				dict[s] += 1
    	if len(dict) is 1:
    		name = list(dict.keys())[0]
    		count = dict[name]
    		res += str(count) + str(name)
    	return res
