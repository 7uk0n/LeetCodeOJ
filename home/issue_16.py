__author__ = 'garfield'


class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        res = num[0] + num[1] + num[-1]
        length = len(num)
        for i in xrange(0, length - 2):
            j, k = i + 1, length - 1
            while j < k:
                __sum = num[i] + num[j] + num[k]
                if abs(__sum - target) < abs(res - target):
                    res = __sum
                if __sum < target:
                    j += 1
                else:
                    k -= 1
        return res


if __name__ == '__main__':
    print Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82)