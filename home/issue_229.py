__author__ = 'wuzehuai'


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        c1, c2 = 0, 0
        can1, can2 = None, None
        for i in nums:
            if i == can1:
                c1 += 1
            elif i == can2:
                c2 += 1
            elif c1 == 0:
                can1, c1 = i, 1
            elif c2 == 0:
                can2, c2 = i, 1
            else:
                c1 -= 1
                c2 -= 1
        res = [n for n in (can1, can2) if nums.count(n) > len(nums) / 3]
        return res


if __name__ == '__main__':
    print Solution().majorityElement([1, 2, 3, 1])
