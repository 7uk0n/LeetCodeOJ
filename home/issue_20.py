__author__ = 'garfield'


class Solution:
    # @return a boolean
    def isValid(self, s):
        temp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch == ')' or ch == ']' or ch == '}':
                if stack and temp[ch] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    stack.append(ch)
                    break
            stack.append(ch)
        return False if stack else True


if __name__ == "__main__":
    solution = Solution()
    a = "()()(){}{}"
    b = "()(})(){}{}"
    c = "((({{}})))[]"
    d = "((({[{[]}]})))[]"
    e = "[])"
    st = a, b, c, d, e
    for x in st:
        print solution.isValid(x)