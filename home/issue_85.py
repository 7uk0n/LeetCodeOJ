__author__ = 'garfield'

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        res = s.split()
        return len(res[-1]) if res else 0



if __name__ == '__main__':
    print Solution().lengthOfLastWord('hello world')
    print Solution().lengthOfLastWord('hello world ddsa ')
    print Solution().lengthOfLastWord('hello world ff')
    print Solution().lengthOfLastWord('')