__author__ = 'garfield'


class Solution:
    # @return a string
    def convert(self, s, nRows):
        result = ''
        length = 2 * nRows - 2
        for i in xrange(nRows):
            poi = i
            x = 1
            while poi < len(s):
                temp = s[poi]
                poi = length * x - poi
                x += 1
                result += temp
        return result


if __name__ == '__main__':
    print Solution().convert("PAYPALISHIRING", 3)