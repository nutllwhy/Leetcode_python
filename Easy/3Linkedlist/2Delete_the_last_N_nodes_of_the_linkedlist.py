# 删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 说明：给定的 n 保证是有效的。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # https://blog.csdn.net/coder_orz/article/details/51691267
        # 删除倒数第n个结点
        def remove(node):
        	if not node:
        		return 0, node
        	index, node.next = remove(node.next)
        	next_node = node if n != index+1 else node.next
        	return index+1, next_node

        ind, new_head = remove(head)
        return new_head

        # 用两个指针，一个快指针从前向后扫描整个链表，一个慢指针比快指针晚出发n+1步
        # 当快指针指向尾部NULL时，慢指针指向要删除结点的前一个结点
        # 由于可能会删除头结点，所以伪装一个头结点方便操作
        new_head = ListNode(0)
        new_head.next = head
        fast = slow = new_head
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return new_head.next
