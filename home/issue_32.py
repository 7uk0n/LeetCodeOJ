# coding=utf-8
__author__ = 'garfield'


class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if len(s) <= 1: return 0
        stack = 0
        max_ = [0]*len(s)
        maxlen = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack += 1
            if c == ')':
                if stack > 0:
                    stack -= 1
                    max_[i] = max_[i-1] + 2
                    if i - max_[i] >= 0:
                        max_[i] += max_[i - max_[i]]
            maxlen = max(max_[i],maxlen)
        return maxlen


if __name__ == '__main__':
    print Solution().longestValidParentheses('(()(((()')
    print Solution().longestValidParentheses('(()')
    print Solution().longestValidParentheses('(()()')
    print Solution().longestValidParentheses('())(()')
    print Solution().longestValidParentheses('(((())))()()')
