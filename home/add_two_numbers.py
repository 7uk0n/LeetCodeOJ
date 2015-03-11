__author__ = 'garfield'
# issue 4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, x):
        self.next = x
        return self

        # def ____(self):
        #     self = self.next


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        f, s = l1, l2
        carry = 0
        head = tail = ListNode(0)
        while f or s or carry:
            result = carry
            if f:
                result += f.val
                f = f.next
            if s:
                result += s.val
                s = s.next
            tail.next = tail = ListNode(result % 10)
            carry = result / 10
        return head.next

def bulk_create(args):
    head = ListNode(args.pop(0))
    l = head
    for i in args:
        l.next = ListNode(i)
        l = l.next
    return head


if __name__ == '__main__':
    first = bulk_create([0,2,3])
    second = bulk_create([0,1,2])
    s = Solution().addTwoNumbers(first, second)
    while True:
        if s:
            print s.val
            s = s.next
        else:
            break
