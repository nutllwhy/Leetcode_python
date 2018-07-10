# 三数之和
# 给定一个包含 n 个整数的数组 nums，
# 判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 方法一：对整个数组排序，二分法逼近结果
        nums.sort()
        res = []
        i = 0
        while(i < len(nums) - 2):
            if(nums[i] != nums[i-1] or i==0):
                target = 0 - nums[i]
                left = i + 1
                right = len(nums) - 1
                while(left != right):
                    if(nums[left] + nums[right] == target):
                        res.append([nums[i],nums[left],nums[right]])
                        while(left < right):
                            left += 1
                            if(nums[left] != nums[left - 1]):
                                break
                        while(right > left):
                            right -= 1
                            if(nums[right] != nums[right + 1]):
                                break
                    elif(nums[left] + nums[right] > target):
                        right -= 1
                    elif(nums[left] + nums[right] < target):
                        left += 1
            i += 1
        return res

        # 方法二：哈希表
        freq = {}
        for elem in nums:
            freq[elem] = freq.get(elem, 0) + 1
        if 0 in freq and freq[0] > 2:
            res = [[0,0,0]]
        else:
            res = []
        # 按数字的正负分开，并排序
        # 如果和为0，那么结果中一定有正有负
        neg = sorted((filter(lambda x: x < 0, freq)))
        nneg = sorted((filter(lambda x: x>= 0, freq)))
        for elem1 in neg:
            for elem2 in nneg:
                target = -(elem1 + elem2)
                # 从正负表中各取一个数字，然后在总表中寻找剩下的那个数字
                if target in freq:
                	# 此target为elem1, elem2其中一个（有重复数字）
                    if target in (elem1, elem2) and freq[target] > 1: 
                        res.append([elem1, target, elem2])
                    # 此target不为elem1或elem2（无重复数字）
                    elif target < elem1 or target > elem2: 
                        res.append([elem1, target, elem2])
        return res