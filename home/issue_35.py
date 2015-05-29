# coding=utf-8
__author__ = 'garfield'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    # 最好使用二分查找
    def searchInsert(self, nums, target):
        for index, v in enumerate(nums):
            if v > target:
                return index
        return len(nums)

    def binarysearchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low+high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low



if __name__ == '__main__':
    print Solution().binarysearchInsert([1, 3, 5, 6], 0)
    print Solution().binarysearchInsert([1, 3, 5, 6], 2)
    print Solution().binarysearchInsert([1, 3, 5, 6], 5)
    print Solution().binarysearchInsert([1, 3, 5, 6], 7)