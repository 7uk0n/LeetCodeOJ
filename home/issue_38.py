__author__ = 'garfield'


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
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