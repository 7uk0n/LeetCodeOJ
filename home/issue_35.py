__author__ = 'garfield'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        for index, v in enumerate(nums):
            if v > target:
                return index
        return len(nums)


if __name__ == '__main__':
    print Solution().searchInsert([1, 3, 5, 6], 0)
    print Solution().searchInsert([1, 3, 5, 6], 2)
    print Solution().searchInsert([1, 3, 5, 6], 5)
    print Solution().searchInsert([1, 3, 5, 6], 7)