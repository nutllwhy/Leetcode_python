# 缺失数字
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：排序，时间复杂度为O（nlogn）
        n = len(nums)
        nums.sort()
        for i in range(n):
        	if nums[i] != i:
        		return i
        return n

        # 方法二：数学方法
        # 用等差数列求和公式求出和，减去给定数组的和，得到缺失的数字
        # https://blog.csdn.net/u014251967/article/details/52473505
        should_sum = int(len(nums) * (len(nums) + 1) / 2)
        now_sum = sum(nums)
        return should_sum - now_sum

        # 方法三：位运算
        # a^0=a 
		# a^b^a=b 
        res = len(nums)
        for i in range(len(nums)):
        	res ^= (i ^ nums[i])
        return res 