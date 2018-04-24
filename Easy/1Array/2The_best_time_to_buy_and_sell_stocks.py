# 买卖股票的最佳时机：
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 解题思路：理论上，为了获取最大利润，只要后一天比第一天高，就应该执行买入卖出操作。

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0
     
        total = 0
        i = 1

        while i < len(prices):
        	diff = prices[i] - prices[i - 1]
        	if diff > 0:
        		total = total + diff
        	i = i + 1
        return total
