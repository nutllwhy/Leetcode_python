# 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 解题思路：因为只会存在一个多余的数字，想办法排除它，可以先对列表进行排序
# 然后只要比较前面两个数字是否相同，相同的，删去，不相同的，直接返回nums[0]
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
        	return nums[0]
        else:
        	nums.sort()
        	while (len(nums) != 1) and (nums[0] == nums[1]):
        		del nums[1],nums[0]
        	return nums[0]