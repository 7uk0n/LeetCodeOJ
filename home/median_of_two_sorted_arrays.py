# coding=utf-8
# issue 2
"""
    设A、B的中间值为mid_a,mid_b，如果这两个值之和大于K，则砍掉必然不包括K的后半个数组，
    如果这两个值之和小于K，砍掉必然不包括K的前半个数组，然后求新数组的第 K - mib_x - 1 个值
"""
class Solution:
    # @return a float
    @classmethod
    def findMedianSortedArrays(self, A, B):
        def findkth(arr_a, arr_b, k):
            mid_a = len(arr_a) / 2
            mid_b = len(arr_b) / 2
            if not arr_a:
                return arr_b[k]
            if not arr_b:
                return arr_a[k]
            if mid_a + mid_b >= k:
                if arr_a[mid_a] > arr_b[mid_b]:
                    return findkth(arr_a[:mid_a], arr_b, k)
                else:
                    return findkth(arr_a, arr_b[:mid_b], k)
            else:
                if arr_a[mid_a] > arr_b[mid_b]:
                    return findkth(arr_a, arr_b[mid_b+1:], k-mid_b-1)
                else:
                    return findkth(arr_a[mid_a+1:], arr_b, k-mid_a-1)

        length = len(A) + len(B)
        if length % 2:
            return findkth(A, B, length / 2)
        else:
            return (findkth(A, B, length / 2)+findkth(A, B, length / 2 - 1)) / 2.0


if __name__ == '__main__':
    a = []
    b = [2, 3]
    c = [2, 3, 4, 5, 7, 8, 9, 19]
    d = [1, 2, 5]
    e = [6, 9, 10, 11]
    f = [1, 5, 7, 8]
    g = [1, 9]
    # print sorted(a + b)
    # print Solution.findMedianSortedArrays(a, b)
    # print '=' * 22
    # print sorted(c + b)
    # print Solution.findMedianSortedArrays(c, b)
    # print '=' * 22
    # print sorted(f + b)
    # print Solution.findMedianSortedArrays(f, b)
    # print '=' * 22
    # print sorted(e + f)
    # print Solution.findMedianSortedArrays(e, f)
    # print '=' * 22
    print sorted(e + d)
    print Solution.findMedianSortedArrays(e, d)
    print '=' * 22
    # print sorted(f + f)
    # print Solution.findMedianSortedArrays(f, f)
