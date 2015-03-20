__author__ = 'garfield'


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = []
        i = 0
        length = len(num)
        while i < length - 2:
            j, k = i + 1, length - 1
            while j < k:
                __sum = num[i] + num[j] + num[k]
                if __sum == 0:
                    res.append([num[i], num[j], num[k]])
                    j += 1
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
                elif __sum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < length - 2 and num[i] == num[i - 1]:
                i += 1
        return res


if __name__ == '__main__':
    a = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(a)