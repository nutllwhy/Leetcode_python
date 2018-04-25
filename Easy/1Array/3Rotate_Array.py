# 旋转数组
# 将包含 n 个元素的数组向右旋转 k 步。
# 例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。

# 解题思路：先全部翻转，然后翻转前k个，再翻转后n-k个。
# 如果k>n，反复操作是无意义的，所以加上一步k%n，取模
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[0 : n] = list(reversed(nums[0 : n]))
        nums[0 : k] = list(reversed(nums[0 : k]))
        nums[k : n] = list(reversed(nums[k : n]))