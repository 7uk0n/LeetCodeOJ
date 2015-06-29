__author__ = 'garfield'


class Solution:
    def trap(self, bars):
        if len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume

    def trap_2(self, bars):
        length = len(bars)
        if len(bars) < 3:
            return 0
        volume = 0
        maxL = [0] * len(bars)
        maxR = [0] * len(bars)
        max_v = bars[0]
        maxL[0] = 0
        for i in xrange(1, length - 1):
            maxL[i] = max_v
            if max_v < bars[i]:
                max_v = bars[i]
        max_v = bars[length - 1]
        maxR[length - 1] = 0
        for i in xrange(length - 1, 0, -1):
            maxR[i] = max_v
            ctrap = min(maxL[i], maxR[i])-bars[i]
            if ctrap > 0:
                volume += ctrap
            if max_v < bars[i]:
                max_v = bars[i]
        return volume

if __name__ == '__main__':
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print Solution().trap_2([0,1,0,2,1,0,1,3,2,1,2,1])
