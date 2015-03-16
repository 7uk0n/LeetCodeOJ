__author__ = 'garfield'
class Solution:
    def hammingWeight(self, n):
        return bin(n).count('1')

    def hammingWeight_2(self, n):
        results = 0
        for i in xrange(32):
            results +=  ((n>>i)&1)
        return results