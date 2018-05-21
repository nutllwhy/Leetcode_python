# 合并两个有序链表
# 将两个有序链表合并为一个新的有序链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
        	return l2
        elif l2 == None:
        	return l1
        newhead = None
        if l1.val < l2.val:
        	newhead = l1
        	newhead.next = self.mergeTwoLists(l1.next, l2)
        else:
        	newhead = l2
        	newhead.next = self.mergeTwoLists(l2.next, l1)
        return newhead
