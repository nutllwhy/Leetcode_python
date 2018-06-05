# Shuffle an Array
# 打乱一个没有重复元素的数组。

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # 复制数组操作
        nums_new = self.nums[:]
        # 原地打乱，python自带shuffle函数
        random.shuffle(nums_new)
        return nums_new
        ########分割线#########
        n = len(nums_new)
        for i in range(n):
        	# randint:生成一个指定范围内的整数
        	j = random.randint(i,n-1)
        	# 互换
        	nums_new[i], nums_new[j] = nums_new[j], nums_new[i]
        return nums_new
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()