# 质数计数
# Count the number of prime numbers less than a non-negative number, n.

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 解法：厄拉多塞筛法
        # https://blog.csdn.net/github_39261590/article/details/73864039
        # 将除了1之外的数放入表中，先圈出2，然后把2的倍数去掉，接下来圈出没有被去掉的下一项（3）
        # 然后再把3的所有倍数都去掉，以此操作到终点
        # 只需要遍历[2,根号n]，根号n之后没有划去的数都是素数
        if n < 3: 
        	# n<3的最大情况：n=2，数列中只有0和1
        	return 0 
        # 初始化一个0~n-1的数列，每一项都是True
        primes = [True] * n
        # 把0和1去掉
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5)+1):
        	if primes[i]:
        		# 把i的倍数去掉
        		# 切片写法：从i*i开始操作，到n结束，每次+i
        		primes[i*i: n: i] = [False] * len(primes[i*i: n: i])
        		# 循环写法
        		for i in range(i*i,n,i):
        			primes[i] = False
        return sum(primes)