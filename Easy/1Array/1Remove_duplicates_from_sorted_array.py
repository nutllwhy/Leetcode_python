# 删除排序数组中的重复项
# 给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
# 不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
        	if nums[i] == nums[i+1]:
        		nums.remove(nums[i])
        	else:
        		i = i +1
        return len(nums)