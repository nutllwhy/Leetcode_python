# 移动零
# 给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。
# 例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。
# 注意事项:
#     必须在原数组上操作，不要为一个新数组分配额外空间。
#     尽量减少操作总数。

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = len(nums)

        while index < n:
        	if nums[index] == 0:
        		nums.append(nums.pop(index))
        		n = n - 1
        	else:
        		index = index + 1