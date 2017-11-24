# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        link1 = l1
        link2 = l2
        head = ListNode(0)
        pivot = head
        carryover = False
        while link1 is not None or link2 is not None:
            if link1 is None:
                s = link2.val
            elif link2 is None:
                s = link1.val
            else:
                s = link1.val + link2.val
            if carryover is True:
                s = s + 1
            if s >= 10:
                s = s - 10
                carryover = True
            else:
                carryover = False
            node = ListNode(s)
            pivot.next = node
            pivot = node
            if link1 is not None:
                link1 = link1.next
            if link2 is not None:
                link2 = link2.next
        if carryover is True:
            pivot.next = ListNode(1)
        if head.next is not None:
            return head.next

#special case [5] [5]



