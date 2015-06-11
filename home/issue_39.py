__author__ = 'garfield'


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        stack = [(0, 0, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for n in range(start, len(candidates)):
                t = total + candidates[n]
                if t > target:
                    break
                stack.append((t, n, res + [candidates[n]]))
        return result


if __name__ == '__main__':
    print Solution().combinationSum([2, 3, 4, 5, 6, 7], 7)