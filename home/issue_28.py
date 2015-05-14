# coding=utf-8
__author__ = 'garfield'


class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        # boyer-moore 算法
        def generateBadCharShift(term):
            skip_list = {}
            for i in range(0, len(term) - 1):
                skip_list[term[i]] = len(term) - i - 1
            return skip_list

        def findSuffixPosition(badchar, suffix, full_term):
            for offset in range(1, len(full_term) + 1)[::-1]:
                flag = True
                for suffix_index in range(0, len(suffix)):
                    term_index = offset - len(suffix) - 1 + suffix_index
                    if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                        pass
                    else:
                        flag = False
                term_index = offset - len(suffix) - 1
                if flag and (term_index <= 0 or full_term[term_index - 1] != badchar):
                    return len(full_term) - offset - 1

        def generateSuffixShift(key):
            skip_list = {}
            buffer = ""
            for i in range(0, len(key)):
                skip_list[len(buffer)] = findSuffixPosition(key[len(key) - i - 1], buffer, key)
                buffer = key[len(key) - i - 1] + buffer
            return skip_list

        goodSuffix = generateSuffixShift(needle)
        badchar = generateBadCharShift(needle)
        i = 0
        while i < len(haystack) - len(needle) + 1:
            j = len(needle)
            while j > 0 and needle[j - 1] == haystack[i + j - 1]:
                j -= 1
            if j > 0:
                badcharshift = badchar.get(haystack[i + j - 1], len(needle))
                goodSuffixshift = goodSuffix[len(needle) - j]
                i += max(badcharshift, goodSuffixshift)
            else:
                return i
        return -1

    def strStr2(self, haystack, needle):
        # kmp 算法
        m, n = len(needle), len(haystack)
        if m == 0: return 0
        if m > n: return -1
        i, k = 0, 0
        for j in xrange(n):
            if i > 0:
                if haystack[j] == needle[k]:
                    k += 1
                else:
                    k = 1 if haystack[j] == needle[0] else 0  # !!!
            if haystack[j] == needle[i]:
                i += 1
            else:
                i = k
                k = 1 if i > 0 and haystack[j] == needle[0] else 0  # !!!
            if i == m: return j - m + 1
        return -1


if __name__ == '__main__':
    block = "This is a simple example"
    print "This is an example search on the string \"", block, "\"."
    print "ple  :", Solution().strStr2(block, "ab")
    print "example :", Solution().strStr2(block, "example")
    print "simple :", Solution().strStr2(block, "simple")
    print " imple :", Solution().strStr2(block, " imple")

