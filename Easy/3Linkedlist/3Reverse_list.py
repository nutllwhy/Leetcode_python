# 反转链表
# 反转一个单链表。

# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://blog.csdn.net/u011452172/article/details/78127836
        # 方法一：用一个数组把链表内容存下来，对数组进行翻转操作
        # 再把数组转成链表
        if head==None or head.next == None:
        	return head
        arr = []
        while head:
        	arr.append(head.val)
        	head = head.next
        newhead = ListNode(0)
        tmp = newhead
        for i in arr[::-1]:
        	tmp.next = ListNode(i)
        	tmp = tmp.next
        return newhead.next