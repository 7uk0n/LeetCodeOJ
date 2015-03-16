# coding=utf-8
import time

__author__ = 'garfield'


class Solution:
    # @return a boolean
    # method 1
    # 带缓存的递归算法，不带缓存，效率非常低
    def __init__(self):
        self.count = 0
        self.cache = {}

    def isMatch(self, s, p):
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not s:
            while len(p) > 1 and p[1] == '*':
                p = p[2:]
            result = not bool(p)
            return result
        if len(p) > 1 and p[1] == '*':
            if self.isMatch(s, p[2:]):
                self.cache[(s, p)] = True
                return True
            elif s[0] == p[0] or p[0] == '.':
                self.cache[(s, p)] = self.isMatch(s[1:], p)
                return self.cache[(s, p)]
            else:
                self.cache[(s, p)] = False
                return False
        elif len(p) > 0:
            if s[0] == p[0] or p[0] == '.':
                self.cache[(s, p)] = self.isMatch(s[1:], p[1:])
                return self.cache[(s, p)]
            else:
                self.cache[(s, p)] = False
                return False
        else:
            self.cache[(s, p)] = False
            return False



if __name__ == '__main__':
    s = Solution()
    # print s.isMatch('aa','aa')
    print s.isMatch('aaa','a*a')
    print s.isMatch('aaba','ab*a*c*a')

    # print s.isMatch('aa','aaaaa')
    # print s.isMatch("abcd", "d*")
    # print s.isMatch("ab", ".*c")
    # print s.isMatch("aaa", "aa")
    # print s.isMatch("aa", "a*")
    # print s.isMatch("aa", ".*")
    # print s.isMatch("ab", ".*")
    # print s.isMatch("aaa", "a*a")
    # print s.isMatch("a", "ab*a")
    # print s.isMatch("a", "ab*")
    print s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
