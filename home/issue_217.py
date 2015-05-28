# coding=utf-8
__author__ = 'garfield'


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    # python 风格
    def containsDuplicate(self, nums):
        return False if len(set(nums)) == len(nums) else True
