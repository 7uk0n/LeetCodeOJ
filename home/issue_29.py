__author__ = 'garfield'

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        sign = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
        result = result if sign else -result
        return min(max(-27147483648, result), 2147483647)

if __name__ == '__main__':
    print Solution().divide(20, 4)
