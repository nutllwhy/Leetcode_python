# 两个数组的交集 II
# 给定两个数组，写一个方法来计算它们的交集。
# 例如:给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].
# 注意：
#    1.输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
#    2.我们可以不考虑输出结果的顺序。
# 跟进:
#    1.如果给定的数组已经排好序呢？你将如何优化你的算法？
#    2.如果 nums1 的大小比 nums2 小很多，哪种方法更优？
#    3.如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？

# 解题思路：先对两个数组进行排序，然后用两个指针标记位置，比较指示区域数字是否一致：一致的进结果数组；不一致的，比较指示区域数字的大小，小的指针向后挪一位

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1.sort()
        nums2.sort()
        index1, index2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while index1 < n1 and index2 < n2:
        	if nums1[index1] == nums2[index2]:
        		result.append(nums1[index1])
        		index1 += 1
        		index2 += 1
        	elif nums1[index1] > nums2[index2]:
        		index2 += 1
        	else:
        		index1 += 1
        return result