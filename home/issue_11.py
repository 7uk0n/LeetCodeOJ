class Solution:
    # @return an integer
    # method 1
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_cap = (right - left) * min(height[left], height[right])
        while left + 1 < right:
            max_cap = max(max_cap, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_cap

    # method 2
    def maxArea_2(self, height):
        left = 0
        right = len(height) - 1
        m_l = height[left]
        m_r = height[right]
        max_cap = (right - left) * min(m_l, m_r)
        while left + 1 < right:
            if height[left] < height[right]:
                left += 1
                if height[left] > m_l:
                    m_l = height[left]
                    max_cap = max(max_cap, (right - left) * min(m_l, m_r))
            else:
                right -= 1
                if height[right] > m_r:
                    m_r = height[right]
                    max_cap = max(max_cap, (right - left) * min(m_l, m_r))
        return max_cap

a = [10,14,10,4,10,2,6,1,6,12]
b = [1,1]
c = [3,6,2,1,2,4,8,9]
print Solution().maxArea_2(a)
print Solution().maxArea_2(b)
print Solution().maxArea_2(c)