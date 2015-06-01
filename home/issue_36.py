__author__ = 'garfield'


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        row_temp = [[] for i in range(9)]
        line_temp = [] * 9
        group_temp = [[] for i in range(9)]
        for index, row in enumerate(board):
            for i, v in enumerate(row):
                block_num = i / 3 + (index / 3) * 3
                if v in row_temp[i] or v in line_temp or v in group_temp[block_num]:
                    return False
                if v != '.':
                    row_temp[i].append(v)
                    line_temp.append(v)
                    group_temp[block_num].append(v)
            line_temp = []
        return True


if __name__ == '__main__':
    a = '.'
    x = [
        [5, 3, a, a, 7, a, a, a, a, ],
        [6, a, a, 1, 9, 5, a, a, a, ],
        [a, 9, 8, a, a, a, a, 6, a, ],
        [8, a, a, a, 6, a, a, a, 3, ],
        [4, a, a, 8, a, 3, a, a, 1, ],
        [7, a, a, a, 2, a, a, a, 6, ],
        [a, 6, a, a, a, a, 2, 8, a, ],
        [a, a, a, 4, 1, 9, a, a, 5, ],
        [a, a, a, a, 8, a, a, 7, 9, ]

    ]
    z = ["....5..1.",
         ".4.3.....",
         ".....3..1",
         "8......2.",
         "..2.7....",
         ".15......",
         ".....2...",
         ".2.9.....",
         "..4......"]

    y = ["..4...63.",
         ".........",
         "5......9.",
         "...56....",
         "4.3.....1",
         "...7.....",
         "...5.....",
         ".........",
         "........."]
    # print Solution().isValidSudoku(x)
    print Solution().isValidSudoku(y)
    print Solution().isValidSudoku(z)