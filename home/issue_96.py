__author__ = 'wuzehuai'

class Solution(object):
    cache = {
        0: 1,
        1: 1,
        2: 2
    }
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = self.cache.get(n) or 0
        if result:
            return result
        for i in xrange(n):
            result += self.numTrees(i) * self.numTrees(n-i-1)
        self.cache[n] = result
        return result

    def numTrees_2(self, n):
        if n == 1 or n == 2:
            return n
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for s in range(1, i+1):
                res[s] += res[s-1] * res[i-s]
        return res[n]

if __name__ == '__main__':
    print Solution().numTrees(19)
