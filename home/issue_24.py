__author__ = 'garfield'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return None
        pseu_head = first = ListNode(0)
        second = head
        first.next = second
        while second and second.next:
            third = second.next
            third.next, second.next = second, third.next
            first.next = third
            first = first.next.next
            second = second.next
        return pseu_head.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    # a.next.next.next = ListNode(4)
    x = Solution().swapPairs(a)
    while x:
        print x.val
        x = x.next