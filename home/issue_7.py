__author__ = 'garfield'
import math

#issue 7
class Solution:
    # @return an integer
    def reverse(self, x):
        new_x = int(str(abs(x))[::-1])
        return (new_x < math.pow(2,31)) * new_x * cmp(x, 0)