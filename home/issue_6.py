# coding=utf-8
# issue 6
__author__ = 'garfield'


class Solution:
    # @return a string
    # method 1 O(n^2)
    """
        跳跃读取同一行的数据，并追加到结果中
    """
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        result = ''
        length = 2 * nRows - 2
        total_len = len(s)
        for i in xrange(nRows):
            poi = i
            step = length - 2 * i
            while poi < total_len:
                if step:
                    temp = s[poi]
                    result += temp
                    poi += step
                step = length - step
        return result

    # method 2 O(n)

    """
        遍历一边字符串数组，将同一行的字符append到同一个res[index]下，index为行数，之后将字符串合并
    """
    def convert_2(self, s, n):
        if n == 1:
            return s
        res = [''for _ in range(n)]
        index = 0
        step = 1
        for i in range(len(s)):
            res[index] += s[i]
            if index == n-1:
                step = -1
            elif index == 0:
                step = 1
            index += step
        return ''.join(res)


if __name__ == '__main__':
    print Solution().convert_2("PAYPALISHIRING", 3)