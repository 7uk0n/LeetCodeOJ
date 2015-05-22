__author__ = 'garfield'


class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not words:
            return []
        length = len(words[0])
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        res = []
        for k in range(length):
            left = k
            subd = {}
            count = 0
            for j in xrange(k, len(s) - length + 1, length):
                tar_word = s[j:j + length]
                if tar_word in d:
                    if tar_word in subd:
                        subd[tar_word] += 1
                    else:
                        subd[tar_word] = 1
                    count += 1
                    while subd[tar_word] > d[tar_word]:
                        subd[s[left:left + length]] -= 1
                        left += length
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    left = j + length
                    subd.clear()
                    count = 0
        return res

if __name__ == '__main__':
    print Solution().findSubstring('barfoobarthefoobarman', ["foo", "bar"])