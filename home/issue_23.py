__author__ = 'garfield'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        value = []
        lists = filter(lambda x: x is not None, lists)
        for l in lists:
            while l:
                value.append(l)
                l = l.next
        value.sort(key=lambda x: x.val)
        node = head = ListNode(0)
        for i in value:
            node.next = i
            node = node.next
        return head.next

    def method_2(self, lists):
        lists = filter(lambda x: x is not None, lists)
        node = head = ListNode(0)
        while lists:
            t = min(lists, key=lambda x: x.val)
            lists[lists.index(t)] = t.next
            node.next = t
            node = node.next
            lists = filter(lambda x: x is not None, lists)
        return head.next

if __name__ == '__main__':
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    node = a
    for i in xrange(3, 20, 3):
        node.next = ListNode(i)
        node = node.next
    node = b
    for i in xrange(4, 20, 3):
        node.next = ListNode(i)
        node = node.next
    node = c
    for i in xrange(5, 20, 3):
        node.next = ListNode(i)
        node = node.next
    # for i in [a, b, c]:
    # while i:
    #         print i.val
    #         i = i.next
    x = Solution().method_2([a])
    while x:
        print x.val
        x = x.next