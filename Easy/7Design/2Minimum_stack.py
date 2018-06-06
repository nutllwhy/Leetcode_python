# 最小栈
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # 前半部分是我的写法，耗时长
        self.nums.append(x)
        # 定义栈里每个元素为一个元组(x, cur_min)表示当前元素和截至当前元素时的最小值。
        # 不管栈怎么变化，总可以常数时间执行四种操作。
        pre_min = 2147483647 if len(self.nums) == 0 else self.nums[-1][1]
        cur_min = min(x,pre_min)
        self.nums.append((x,cur_min))
        

    def pop(self):
        """
        :rtype: void
        """
        del self.nums[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]
        # 写法分割线
        return self.nums[-1][0]

        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.nums)
        # 写法分割线
        return self.nums[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()