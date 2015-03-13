__author__ = 'garfield'
# issue 5
class Solution:
    # @return a string
    # method 1 o(n^2)
    def longestPalindrome(self, s):
        if not s:
            return []
        max_len = 1
        start = 0
        for i in xrange(len(s)):
            if i-max_len >=1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1
                max_len+=2
                continue
            if i-max_len >=0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i - max_len
                max_len+=1
        return s[start:start+max_len]
    # method 2 o(n)