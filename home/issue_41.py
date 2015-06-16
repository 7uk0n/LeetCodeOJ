__author__ = 'garfield'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in xrange(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                k = nums[i] - 1
                nums[i], nums[k] = nums[k], nums[i]
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1


if __name__ == '__main__':
    print Solution().firstMissingPositive([2,1])