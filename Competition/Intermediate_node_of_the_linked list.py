# 链表的中间结点
# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNodeS
        """
        temp = head
        mid = head
        # 两个指针同时开始从头遍历，一个快指针一次走2步，一个慢指针一次走一步
        # 快指针走到底的时候，慢指针刚好到中间
        while head != None and head.next != None:
        	head = head.next.next
        	temp = temp.next
        	mid = temp
        return mid