__author__ = 'wuzehuai'

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int height
        :type n: int width
        :rtype: int
        """
        m -= 1
        n -= 1
        if not m or not n:
            return 1
        k = m + n
        s = m if m < n else n
        numerator = reduce(lambda x, y: x*y, range(1, k+1), 1)
        denominator_1 = reduce(lambda x, y: x*y, range(1, s+1), 1)
        denominator_2 = reduce(lambda x, y: x*y, range(1, k-s+1), 1)
        return int(numerator/(denominator_1*denominator_2))


if __name__ == '__main__':
    print Solution().uniquePaths(2, 2)