# 爬楼梯
# 假设你正在爬楼梯。需要 n 步你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://blog.csdn.net/guoziqing506/article/details/51646800
        # 走到第i级台阶的走法:f[i] = f[i - 1] + f[i - 2]
        record = [1,1]
        if n >= 2:
        	for i in range(2, n + 1):
        		record.append(record[i - 1] + record[i - 2])
        return record[n]