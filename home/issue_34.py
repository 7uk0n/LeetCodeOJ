__author__ = 'garfield'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        def firstgreaterequal(num, tar):
            low, high = 0, len(num)
            while low < high:
                mid = low + ((high - low) >> 1)
                if num[mid] < tar:
                    low = mid + 1
                else:
                    high = mid
            return low

        start = firstgreaterequal(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, firstgreaterequal(nums, target + 1) - 1]

    def searchRange_2(self, nums, target):
        def binarysearch(a, tar):
            low, high = 0, len(a)
            while low < high:
                mid = (low + high) / 2
                if a[mid] < tar:
                    low = mid + 1
                else:
                    high = mid
            return low
        start = binarysearch(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        else:
            return [start, binarysearch(nums, target+1)-1]


if __name__ == '__main__':
    print Solution().searchRange_2([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3)
    print Solution().searchRange_2([1, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3)
    print Solution().searchRange_2([2, 2], 3)
    print Solution().searchRange_2([1, 4], 0)
    print Solution().searchRange_2([1, 2, 3, 3, 3, 3, 3, 3, 3, 8], 3)
