# coding=utf-8
# issue 3
"""
    截取两个相同字母之间的子串加后一个相同字母为最大值，如果子串直接到字符串末尾，
    由于最大长度在出现重复字母时才复值，所以还要比较当前子串到数组末尾的长度
"""
class Solution:

    # @return an integer
    # @classmethod
    def lengthOfLongestSubstring(self, s):
        head = 0
        char_dict = {}
        result = 0
        for index, value in enumerate(s):
            if value in char_dict  and char_dict[value] >= head:
                if index - head > result:
                    result = index-head
                head = char_dict[value]+1
            char_dict[value] = index
        return max(result, len(s)-head)

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('abdcafsfkd')