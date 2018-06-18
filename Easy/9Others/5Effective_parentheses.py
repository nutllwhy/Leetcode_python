# 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 循环字符串，遇左括号入栈。
		# 遇右括号，从栈顶取元素然后配对，判断配对结果。
		# 最后再判断栈是否不为空。
        if s is None:
        	return False

        x = ['{','[','(']
        y = ['}',']',')']
        z = ['{}','[]','()']

        res = []
        for i in s:
        	if i in x:
        		# 左括号入栈
        		res.append(i)
        	elif i in y:
        		if res == []:
        			# s[i]为右括号，但是此时res中没有左括号
        			return False
        		else:
        			# 将栈尾元素（一个左括号）和当前的i配对
        			temp = res.pop(-1) + i
        			if temp not in z:
        				return False
        # 所有元素都入栈or配对，如果res中还有左括号：
        if len(res) != 0:
        	return False
        return True
