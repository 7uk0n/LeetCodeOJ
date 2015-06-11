__author__ = 'garfield'


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        l = len(candidates)

        def combinationSum(i, t, res):
            if t == 0:
                ans.append(list(res))
                return
            for j in xrange(i, l):
                v = candidates[j]
                if j > i and v == candidates[j-1]:
                    continue
                if t < v:
                    break
                res.append(v)
                combinationSum(j+1, t-v, res)
                res.pop()
        combinationSum(0, target, [])
        return ans

if __name__ == '__main__':
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)