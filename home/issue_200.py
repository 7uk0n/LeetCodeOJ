__author__ = 'wuzehuai'


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        height = len(grid)
        width = len(grid[0])
        import copy
        flag = [copy.copy([0] * width) for i in range(height)]
        stack = []
        is_new = True
        x, y = 0, 0
        while y < height:
            for x in range(width):
                if flag[y][x] == 0 and grid[y][x] == "1":
                    stack.append((y, x))
                    y -= 1
                    break
            while stack:
                c_y, c_x = stack.pop()
                flag[c_y][c_x] = 1
                if grid[c_y][c_x] == "1":
                    if is_new:
                        count += 1
                        is_new = False
                    if c_x < width:
                        if c_x > 0 and not flag[c_y][c_x-1] and grid[c_y][c_x-1] == "1":
                            stack.append((c_y, c_x + 1))
                        if c_x + 1 < width and not flag[c_y][c_x+1] and grid[c_y][c_x + 1] == "1":
                            stack.append((c_y, c_x + 1))
                    if c_y < height:
                        if c_y > 0 and not flag[c_y - 1][c_x] and grid[c_y - 1][c_x] == "1":
                            stack.append((c_y + 1, c_x))
                        if c_y + 1 < height and not flag[c_y + 1][c_x] and grid[c_y + 1][c_x] == "1":
                            stack.append((c_y + 1, c_x))
            is_new = True
            y += 1
        return count


if __name__ == '__main__':
    a = ["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"]
    print Solution().numIslands(a)
