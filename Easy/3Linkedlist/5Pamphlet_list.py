# 回文链表
# 请判断一个链表是否为回文链表

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 把链表转成数列，翻转，判断翻转前后是否一致
        if head == None or head.next == None:
        	return True
        arr = []
        while head:
        	arr.append(head.val)
        	head = head.next

        arr2 = arr[::-1]
        if arr == arr2:
        	return True
        else:
        	return False