# coding=utf-8
__author__ = 'wuzehuai'


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        dis_vector = [[0 for i in range(width)] for x in range(height)]
        for i in range(height):
            for j in range(width):
                if obstacleGrid[i][j] == 1:
                    # 障碍物
                    dis_vector[i][j] = 0
                elif i == 0 or j == 0:
                    if j:
                        dis_vector[i][j] = dis_vector[i][j - 1]
                    elif i:
                        dis_vector[i][j] = dis_vector[i - 1][j]
                    else:
                        dis_vector[i][j] = 1
                else:
                    dis_vector[i][j] = dis_vector[i][j - 1] + dis_vector[i - 1][j]
        return dis_vector[-1][-1]


if __name__ == '__main__':
    x = [[0 for i in range(3)] for x in range(3)]
    x[1][1] = 1
    print Solution().uniquePathsWithObstacles([[0]])
