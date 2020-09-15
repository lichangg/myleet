#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 思路:根据board设置一个hashmap表,记录下每个字符出现的坐标, 遍历word字符串,
# 得到当前字符[A]的坐标集合,从该集合里面的每一个坐标出发,找到其下一个坐标只能出现的上下左右位置,然后和下一个字符B在hashmap里面出现的坐标集合对比看看有没有交集
# 无交集则该递归停止,有交集则以此递归对比,对比完word所有字符
# 上述是一刷思路, 可惜超时
class Solution:

    def exist(self, board, word: str) -> bool:
        self.flag = False

        hashmap = {}
        m_max = len(board)
        n_max = len(board[0])
        for index_i, i in enumerate(board):
            for index_j, j in enumerate(i):
                if hashmap.get(j):
                    hashmap[j].append((index_i, index_j))
                else:
                    hashmap[j] = [(index_i, index_j)]

        def dp(coordinate, index, cur_used):
            cur_used.append(coordinate)
            if index == len(word):
                self.flag = True
                return
            m, n = coordinate
            if m == 0 and n == 0:
                prob_coordinate = [(0, 1), (1, 0)]
            elif m == m_max and n == 0:
                prob_coordinate = [(m - 1, 0), (m, 1)]
            elif n == n_max and m == 0:
                prob_coordinate = [(0, n - 1), (1, n)]
            elif m == m_max and n == n_max:
                prob_coordinate = [(m, n - 1), (m - 1, n)]
            else:
                prob_coordinate = [(m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)]
            coordinate = hashmap.get(word[index])
            if not coordinate or not prob_coordinate:
                together_set = None
            else:
                together_set = set(coordinate) & set(prob_coordinate)
            for used in cur_used:
                if together_set and used in together_set:
                    together_set.remove(used)
            if together_set:
                for i in together_set:
                    dp(i, index + 1, cur_used[:])

        if not hashmap.get(word[0]):
            return False

        for coordinate in hashmap.get(word[0]):
            cur_used = []
            dp(coordinate, 1, cur_used)

        return self.flag


class Solution:

    def exist(self, board, word: str) -> bool:

        def dfs(n, cur_word_index, x, y, path):
            if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board):
                return
            if board[y][x] == word[cur_word_index]:
                if n == 1:
                    return True
                else:
                    for i in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        for j in path:
                            if i[0] == j[0] and i[1] == j[1]:
                                break
                        else:
                            path.append((i[0], i[1]))
                            if dfs(n - 1, cur_word_index + 1, i[0], i[1], path[:]):
                                return True
                    # dfs(n - 1, cur_word_index + 1, x + 1, y)
                    # dfs(n - 1, cur_word_index + 1, x - 1, y)
                    # dfs(n - 1, cur_word_index + 1, x, y + 1)
                    # dfs(n - 1, cur_word_index + 1, x, y - 1)

        return dfs(len(word), 0, 0, 0, []) or False


board = [["A", "B", "C", "D"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]
         ]

a = Solution().exist(board, 'SF')
print(a)
