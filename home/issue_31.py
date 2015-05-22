__author__ = 'garfield'


class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        flag = False
        for k in range(-2, -len(nums) - 1, -1):
            # sort num[k:-1]
            ## min_v is the min number which greater than num[k]
            # swap min_v with k then sort num[min_v:] as a desc array
            min_index = k + 1
            for i in range(k + 1, 0, 1):
                if nums[min_index] > nums[i] > nums[k]:
                    min_index = i
            if nums[k] < nums[min_index]:
                flag = True
                nums[k], nums[min_index] = nums[min_index], nums[k]
                temp = nums[k + 1:]
                nums[k + 1:] = []
                nums += sorted(temp)
                break
        if not flag:
            nums.reverse()


if __name__ == "__main__":
    x = [2, 3, 1]
    y = [3, 2, 1]
    z = [1, 2, 3]
    w = [1, 3, 2]
    # Solution().nextPermutation(x)
    # Solution().nextPermutation(y)
    Solution().nextPermutation(z)
    # Solution().nextPermutation(w)
    print x, y, z, w