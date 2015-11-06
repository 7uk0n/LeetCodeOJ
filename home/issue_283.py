__author__ = 'wuzehuai'


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = k = 0
        l = len(nums)
        while k < l:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1
            i += 1
            k += 1
