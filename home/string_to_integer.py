__author__ = 'garfield'
import math


class Solution:
    # @return an integer
    def atoi(self, str):
        s = str.strip()
        if not s:
            return 0
        res=''
        max_v = math.pow(2,31) - 1
        min_v = -math.pow(2,31)
        if s[0] in '+-':
            res+=s[0]
            s = s[1:]
        for i in s:
            if not i.isdigit():
                break
            res+=i
        try:
            res = int(res)
        except:
            return 0
        if res > max_v:
            return max_v
        elif res < min_v:
            return min_v
        else:
            return res

if __name__=='__main__':
    test = [
        '1',
        '+-2',
        '-123412     ',
        '+12      312',
        '-321ja9',
        '   -1 9 2 9 1 ',
    ]
    for i in test:
        print Solution().atoi(i)
