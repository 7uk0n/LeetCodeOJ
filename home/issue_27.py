__author__ = 'garfield'


class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums:
            return 0
        head = tail = 0
        while tail < len(nums) and nums[tail] == val:
            tail += 1
        nums[head], nums[tail] = nums[tail], nums[head]
        tail += 1
        for i in range(tail, len(nums)):
            if nums[i] != val:
                nums[head + 1] = nums[i]
                head += 1
        return 0 if nums[0] == val else head + 1


if __name__ == '__main__':
    x = [1, 2, 2, 3, 4, 5, 1, 1, 1, ]
    y = [1]
    s = Solution().removeElement(y, 1)
    print x[:s]