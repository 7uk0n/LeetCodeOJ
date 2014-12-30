# issue 168
class Solution:
    @classmethod
    def convertToTitle(self, num):
        if num==0:
            return ''
        a=''
        while True:
            d = (num -1) % 26
            a = chr(d+ord('A'))+a
            num = (num - 1) / 26
            if num == 0:
                break
        return a
# anther solution return '' if num==0 else (self.convertToTitle((num-1) / 26) + chr((num-1) % 26 + ord('A')))
if __name__=='__main__':
    print Solution.convertToTitle(28)
    print Solution.convertToTitle(0)
