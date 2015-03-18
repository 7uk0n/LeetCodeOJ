__author__ = 'garfield'
class Solution:
    # @return an integer
    def romanToInt(self, s):
        value_roman = {"M":1000, "D":500,
                       "C":100, "L":50,
                       "X":10, "V": 5,"I": 1}
        last = 0
        total = 0
        for ch in s:
            if value_roman[ch] <= last:
                total += value_roman[ch]
            else:
                total += (value_roman[ch] - 2 * last)
            last = value_roman[ch]
        return total

if __name__ == '__main__':
    print Solution().romanToInt('DCXXI')
    print Solution().romanToInt('CDXXI')
