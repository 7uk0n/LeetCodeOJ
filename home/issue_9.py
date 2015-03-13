__author__ = 'garfield'


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        reverse = 0
        y = x
        while y:
            reverse = reverse * 10 + y % 10
            y /= 10
        return x == reverse