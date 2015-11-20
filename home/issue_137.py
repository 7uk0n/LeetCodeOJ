# coding=utf-8
__author__ = 'wuzehuai'


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def add(a, b):
            for pos in range(32):
                offset = 1 << pos
                temp = a[pos] + (b & offset)
                a[pos] = temp

        res = [0] * 32
        for i in nums:
            add(res, i)
        for i in range(32):
            res[i] = 1 if res[i] % 3 else 0
        res = res[::-1]
        flag = False
        if res[0] == 1:
            flag = True
            res = list(map(lambda x: '0' if x else '1', res))
        else:
            res = list(map(str, res))
        result = int(''.join(res), 2)
        result = -result if flag else result
        return result


if __name__ == '__main__':
    # print Solution().singleNumber([-2, -2, 1, 1, -3, -2, 1, -3, -3])
    class Parent(object):
        x = 0
    class Child(Parent):
        pass
    child = Child()
    print Parent.x, Child.x, child.x
    Parent.x = 3
    print Parent.x, Child.x, child.x
    child.x = 1
    print Parent.x, Child.x, child.x
    Child.x = 2
    print Parent.x, Child.x, child.x

"""
00 1次
01 2次
10 3次 或 0 次

因为这里只需要三种状态，所以 11是不存在的，当运算得到11时，我们转换为00


a b counter  a b
0 0 + 0  =>  0 0
0 1 + 0  =>  0 1
1 0 + 0  =>  1 0
0 0 + 1  =>  0 1
0 1 + 1  =>  1 0
1 0 + 1  =>  0 0

a counter res
0    0     0
0    1
1



   ｜｜
   ｜｜还记不记得计算机里存储long的时候，两个字节，一个字节存高位，一个字节存低位？
   ｜｜用两个32位整形数来存储这个结构的话，a存高位，b存地位
   ｜｜

"""
