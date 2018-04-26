# 存在重复
# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 大笨蛋超时做法orz
        # i = 0
        # flag = 0
        # while i < len(nums):
        # 	j = i + 1
        # 	while j < len(nums):
        # 		if nums[i] == nums[j]:
        # 			flag = 1
        # 			break
        # 		else:
        # 			j = j + 1
        # 	i = i + 1
        # if flag == 1:
        # 	return True
        # else:
        # 	return False

        # 对list去重，判断去重后和去重前的list长度是否一致
        nums2 = list(set(nums))
        if len(nums) == len(nums2):
        	return False
        else:
        	return True


