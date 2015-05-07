__author__ = 'garfield'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1
if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 2])