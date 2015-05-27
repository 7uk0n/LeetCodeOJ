__author__ = 'garfield'


class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, num):
        n = len(num)
        if n == 0 or n == 1: return
        if n == 2:
            num[0], num[1] = num[1], num[0]
            return

        pre = n-1
        imin = n-1

        for i in xrange(n-2, -1, -1):
            if num[i] > num[pre]:
                pre = i
                continue
            else:
                num[i], num[imin] = num[imin], num[i]
                tmp = num[pre:]
                tmp.sort()
                num = num[:pre]+tmp
                return
        if i == -1:
            num.sort()
            return


if __name__ == "__main__":
    x = [2, 3, 1]
    y = [3, 2, 1]
    z = [1, 2, 3]
    w = [1, 3, 2]
    Solution().nextPermutation(z)
    print x, y, z, w