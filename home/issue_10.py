__author__ = 'garfield'


class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def matchone(ch, reg):
            result = ch == reg or (reg == '.' and len(ch) > 0)
            return result
        if not p and not s:
            return not bool(s)
        if len(p) > 1 and p[1] == '*':
            while matchone(s[0], p[0]):
                # return True
                s = s[1:]
                if self.isMatch(s, p[2:]):
                    return True
            if self.isMatch(s, p[2:]):
                return True
        elif len(s) > 0 and len(p) > 0:
            if not matchone(s[0], p[0]):
                return False
            return self.isMatch(s[1:], p[1:])
        return False



if __name__ == '__main__':
    s = Solution()
    print s.isMatch('aa','a')
    print s.isMatch('aa','aaaaa')
    print s.isMatch("abcd", "d*")
    print s.isMatch("ab", ".*c")
    # print s.isMatch("aaa", "aa")
    # print s.isMatch("aa", "a*")
    # print s.isMatch("aa", ".*")
    # print s.isMatch("ab", ".*")
    # print s.isMatch("aab", "c*a*b")