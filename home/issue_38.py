import itertools

__author__ = 'garfield'


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        return '1' if n==1 else ''.join([str(len(x))+x[0] for x in [list(g) for k, g in itertools.groupby(self.countAndSay(n-1))]])
    def countAndSay_2(self, n):
        string = '1'
        result = '1'
        n -= 1
        while n:
            result = ''
            temp = string[0]
            count = 1
            for i in string[1:]:
                if i == temp:
                    count += 1
                else:
                    result += str(count) + temp
                    temp = i
                    count = 1
            result += str(count) + temp
            n -= 1
            string = result
        return result


if __name__ == '__main__':
    print Solution().countAndSay(1)
    print Solution().countAndSay(2)
    print Solution().countAndSay(3)
    print Solution().countAndSay(4)
    print Solution().countAndSay(5)
    print Solution().countAndSay(6)