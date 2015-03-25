__author__ = 'garfield'
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        __key = {
            '1':'1',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
            '*':'*',
            '#':'#',
            '0':'0'
        }
        if not digits:
            return []
        temp = __key[digits[0]]
        result = list(temp)
        for i in digits[1:]:
            temp = []
            for x in result:
                for k in __key[i]:
                    temp.append(x+k)
            result=temp
        return result

if __name__ == '__main__':
    print Solution().letterCombinations('23')
