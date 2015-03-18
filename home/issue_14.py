__author__ = 'garfield'


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        p_len = len(strs[0])
        for i in xrange(1, len(strs)):
            p_len = min(strs[i], p_len)
            while p_len and strs[i][:p_len] != strs[0][:p_len]:
                p_len -= 1
        return strs[0][:p_len]


if __name__ == '__main__':
    a = [
        'aca', 'cba'
    ]
    b = ['', 'b']
    c = ['abc', 'abd', '']
    d = ['aaa', 'a',
         'aa']
    s = [a, b, c, d]
    for i in s:
        print Solution().longestCommonPrefix(i)
