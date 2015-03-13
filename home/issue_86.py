import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    @classmethod
    def partition(self, head, x):
        dummy_head = ListNode(x)
        dummy_head.next = head
        last_p = dummy_head
        current = last_p.next
        greater_head = ListNode(x)
        greater_p = greater_head
        while current:
            print current.val
            if current.val >= x:
                last_p.next = current.next
                current.next = None
                greater_p.next = current
                greater_p = greater_p.next
            else:
                last_p = last_p.next
            current = last_p.next
        last_p.next = greater_head.next
        return dummy_head.next


if __name__ == "__main__":
    head = ListNode(random.randint(1, 20))
    last = head
    # for i in range(10):
    #    temp = ListNode(random.randint(1,20))
    #    last.next=temp
    #    last=last.next 
    t = head
    while t:
        print(str(t.val) + "->"),
        t = t.next
    print ''
    result = Solution.partition(head, 7)
    t = result
    while t:
        print(str(t.val) + "->"),
        t = t.next
