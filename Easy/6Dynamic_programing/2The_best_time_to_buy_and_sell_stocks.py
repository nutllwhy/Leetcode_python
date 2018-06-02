# 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。

# class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 两个循环超时了XD
        res = 0
        for i in range(len(prices)):
        	for j in range(i,len(prices)):
        		profit = prices[j] - prices[i]
        		if profit > res:
        			res = profit
        return res

        # https://blog.csdn.net/guoziqing506/article/details/51434777
        # 最大利润实际上就是每天的交易价格，减去上一天的价格所构成的这个数组的最大子数组
        if len(prices) <= 1:  
            return 0  
        n = len(prices)  
        sum_value = 0  
        max_value = 0  
        for i in range(1, n):  
            sum_value += prices[i] - prices[i - 1]  
            max_value = max(max_value, sum_value)  
            sum_value = max(0, sum_value)  
        return max_value 