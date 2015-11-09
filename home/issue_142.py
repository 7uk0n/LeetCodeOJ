__author__ = 'wuzehuai'
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counter = slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while counter != slow:
                    slow=slow.next
                    counter=counter.next
                return slow
        return None