import collections
import itertools

__author__ = 'garfield'


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        two_sum = collections.defaultdict(list)
        res = set()
        for (n1, i1), (n2, i2) in itertools.combinations(enumerate(num), 2):
            two_sum[i1+i2].append({n1, n2})
        for t in list(two_sum.keys()):
            if not two_sum[target-t]:
                continue
            for pair1 in two_sum[t]:
                for pair2 in two_sum[target-t]:
                    if pair1.isdisjoint(pair2):
                        res.add(tuple(sorted(num[i] for i in pair1 | pair2)))
            del two_sum[t]
        return [list(r) for r in res]


if __name__ == '__main__':
    print Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0)
    print Solution().fourSum([0,0,0,0], 0)
    print Solution().fourSum([-1,0,1,2,-1,-4], -1)