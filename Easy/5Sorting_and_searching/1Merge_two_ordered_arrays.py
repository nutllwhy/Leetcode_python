# 合并两个有序数组
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 皮一下的做法，赋值给后面的0，然后排序
        if  n == 0:
            return
        else:
            for j in range(n):
                nums1[m+j] = nums2[j]
            nums1.sort()

        # 从后往前比
        last, i, j = m + n - 1, m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last, i = last - 1, i - 1
            else:
                nums1[last] = nums2[j]
                last, j = last - 1, j - 1
        # nums2个数比nums1多，继续给last赋值，指针前移
        while j >= 0:
            nums1[last] = nums2[j]
            last, j = last - 1, j - 1