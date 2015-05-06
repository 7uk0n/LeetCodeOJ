__author__ = 'garfield'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None or k < 2:
            return head
        next_head = head
        for i in range(k - 1):
            next_head = next_head.next
            if next_head is None:
                return head
        ret = next_head
        current = head
        while next_head:
            tail = current
            prev = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                _next = current.next
                current.next = prev
                prev = current
                current = _next
            tail.next = next_head or current
        return ret


if __name__ == '__main__':
    node = head = ListNode(0)
    for i in range(1, 5):
        node.next = ListNode(i)
        node = node.next
    res = Solution().reverseKGroup(head, 2)
    while res:
        print res.val
        res = res.next