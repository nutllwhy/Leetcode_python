# 两数之和
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 超慢双循环做法
        # n = len(nums)
        # for i in range(0, n):
        # 	temp = target - nums[i]
        # 	j = i + 1
        # 	while j < n:
        # 		if nums[j] == temp:
        # 			return [i, j]
        # 			break
        # 		else:
        # 			j = j + 1

        # 哈希表，快了120倍
        hash_table = {}
        for i, ele in enumerate(nums):
        	hash_table[ele] = i

        for i, ele in enumerate(nums):
        	temp = target - ele
        	if temp in hash_table.keys() and i < hash_table[temp]:
        		return [i, hash_table[temp]]
