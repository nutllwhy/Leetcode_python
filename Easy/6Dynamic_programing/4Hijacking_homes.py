# 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。
# 每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，
# 计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob_money=0  
        current_money=0  
        for i in nums:  
            # 比较抢这家总值大，还是抢上一家总值大
            # 语法糖，同步赋值
            current_money,rob_money=rob_money,max(rob_money,current_money+i)
        return rob_money