# 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 仿照昨天的做法
        temp_sum = 0  
        max_value = nums[0]  
        for i in range(len(nums)):  
            temp_sum += nums[i]  
            max_value = max(max_value, temp_sum)  
            temp_sum = max(0, temp_sum)  
        return max_value 
        # 每次循环调0做法
        tmp=0
        maxSum=min(nums)
        for i in range(len(nums)):
            if tmp<0:
                tmp=0
            tmp+=nums[i]
            if tmp>maxSum:
                maxSum=tmp
        return maxSu