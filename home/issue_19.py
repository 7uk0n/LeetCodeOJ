__author__ = 'garfield'
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        pesuhead  = ListNode(0)
        pesuhead.next = head
        first = last = pesuhead
        for i in xrange(n):
            first = first.next
            if not first:
                return None
        while first.next:
            first = first.next
            last = last.next
        last.next = last.next.next
        return pesuhead.next


if __name__ == '__main__':
    head = ListNode(0)
    # head.next = ListNode(2)
    tail = head
    for i in xrange(1, 2):
        ln = ListNode(i)
        tail.next = ln
        tail = ln
    tail = head
    while tail:
        print tail.val,
        tail = tail.next
    print ''
    tail = Solution().removeNthFromEnd(head, 2)
    while tail:
        print tail.val,
        tail = tail.next
