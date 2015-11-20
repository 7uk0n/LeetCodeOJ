__author__ = 'wuzehuai'


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        mid = low + (high + low) / 2
        count = 0
        while low != high:
            for i in nums:
                if i < mid:
                    count += 1
            if count <= mid:
                high = mid
            else:
                low = mid
