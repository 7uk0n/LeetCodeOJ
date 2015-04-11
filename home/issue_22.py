__author__ = 'garfield'


class Solution:
    # @param an integer
    # @return a list of string
    def __init__(self):
        self.cache = {}

    def generateParenthesis(self, n, opened=0):
        if n == 0:
            self.cache["%s_%s" % (n, opened)] = [')' * opened]
            return [')' * opened]
        t = self.cache.get("%s_%s" % (n, opened))
        if t:
            return t

        if opened == 0:
            self.cache["%s_%s" % (n, opened)] = ["(" + x for x in self.generateParenthesis(n - 1, 1)]
            return self.cache["%s_%s" % (n, opened)]
        else:
            self.cache["%s_%s" % (n, opened)] = [')' + x for x in self.generateParenthesis(n, opened - 1)] + [
                '(' + x for x in self.generateParenthesis(n - 1, opened + 1)]
            return self.cache["%s_%s" % (n, opened)]

    def method_2(self, n):
        def func(stack, current_str, left, right):
            if not left and not right:
                stack.append(current_str)
            if right > 0:
                func(stack, current_str + ')', left, right-1)
            elif left > 0:
                func(stack, current_str + '(', left-1, right+1)
        res = []
        func(res, '', n, 0)
        return res

if __name__ == '__main__':
    # for i in Solution().generateParenthesis(2):
    # print i
    for i in Solution().method_2(3):
        print i
        # for i in Solution().generateParenthesis(4):
        #     print i
        # for i in Solution().generateParenthesis(5):
        #     print i