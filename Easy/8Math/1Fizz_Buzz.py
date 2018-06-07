# Fizz Buzz
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = []
        for i in range(1,n+1):
        	j = str(i)
        	if i % 15 == 0:
        		j = "FizzBuzz"
        	elif i % 3 == 0:
        		j = "Fizz"
        	elif i % 5 == 0:
        		j = "Buzz"
        	nums.append(j)
        return nums

        
