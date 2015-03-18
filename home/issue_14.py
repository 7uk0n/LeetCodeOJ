__author__ = 'garfield'
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = list(strs[0])
        for s in strs[1:]:
            temp = []
            for ch in s:
                if prefix:
                    p = prefix.pop(0)
                    if p == ch:
                        temp.append(p)
                    else:
                        break
            prefix = temp
        return ''.join(prefix)
    def longestCommonPrefix_2(self, strs):
        if not strs:
            return ''
        p_len = len(strs[0])
        for i in xrange(1, len(strs)):
            p_len = min(strs[i], p_len)
            while p_len and strs[i][:p_len] != strs[0][:p_len]:
                p_len -= 1
        return strs[0][:p_len]
    def longestCommonPrefix_3(self, strs):
        def get_common_prefix(x, y):
            LCP_length = 0
            for i in range(0, min(len(x), len(y))):
                if x[i] != y[i]:
                    break
                LCP_length += 1
            return x[:LCP_length]
        if not strs:
            return ''
        return reduce(get_common_prefix, strs)


if __name__ == '__main__':
    a = [
        'aca', 'cba'
    ]
    b = ['', 'b']
    c = ['abc', 'abd', '']
    d = ['aaa','a',
         'aa']
    s= [a,b,c,d]
    for i in s:
        print Solution().longestCommonPrefix(i)
