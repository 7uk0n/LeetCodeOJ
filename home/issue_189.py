__author__ = 'garfield'


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k = len(nums) - k % len(nums)
        head = nums[0:k]
        nums.__delslice__(0, k)
        nums += head


x = [1,2,3,4,5,6,7]
Solution().rotate(x, 3)
print x