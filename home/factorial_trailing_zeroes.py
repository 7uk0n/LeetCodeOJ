# issue 172
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while True:
            result += n / 5
            n = n / 5
            if n == 0:
                break
        return result
