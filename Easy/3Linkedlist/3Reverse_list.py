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

        # 方法二：新建表头反转，cur循环变量判定，tmp保存数据
        if head == None or head.next == None:
        	return head
        cur = head
        tmp = None
        newhead = None
        while cur:
        	tmp = cur.next
        	cur.next = newhead
        	newhead = cur
        	cur = tmp
        return newhead

        # 方法三：就地反转
        if head == None or head.next == None:
        	return head
        p1 = head
        p2 = head.next
        tmp = None
        while p2:
        	tmp = p2.next
        	p2.next = p1
        	p1 = p2
        	p2 = tmp
        head.next = None
        return p1