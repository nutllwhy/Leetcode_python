# 环形链表
# 给定一个链表，判断链表中是否有环。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
        	return False
        # 设置一个快指针一个慢指针
        # 快指针每次走两步，慢指针每次都一步
        # 如果快指针追上了慢指针，就说明链表有环
        slow = head.next
        fast = slow.next
        while fast and slow:
        	if fast == slow:
        		return True
        	slow = slow.next
        	fast = fast.next
        	# 在快指针进行第二跳之前要先判断是否为空
        	# 指向空的时候不能再跳，会报错
        	if fast:
        		fast = fast.next
        return False