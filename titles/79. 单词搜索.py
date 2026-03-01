#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 思路:根据board设置一个hashmap表,记录下每个字符出现的坐标, 遍历word字符串,
# 得到当前字符[A]的坐标集合,从该集合里面的每一个坐标出发,找到其下一个坐标只能出现的上下左右位置,然后和下一个字符B在hashmap里面出现的坐标集合对比看看有没有交集
# 无交集则该递归停止,有交集则以此递归对比,对比完word所有字符
# 上述是一刷思路, 可惜超时
from typing import List


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

# 从每个点出发递归, 代码简洁得多,也不会超时,不过还是慢
# 执行用时：872 ms, 在所有 Python3 提交中击败了5.01%的用户
# 内存消耗：18.3 MB, 在所有 Python3 提交中击败了5.05%的用户
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
                            path.append((x, y))
                            if dfs(n - 1, cur_word_index + 1, i[0], i[1], path[:]):
                                return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(len(word), 0, j, i, []):
                    return True

        else:
            return False

# 别人的递归, 空间上来说貌似上一个算法用了path记录, 而本算法不记录用过的path, 而是用一个used矩阵记录, 对其是否已经用过的状态进行回溯

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m ,n, l = len(board), len(board[0]), len(word)
        used = [[0]*n for _ in range(m)]
        bias = [(-1,0), (1,0), (0,-1), (0, 1)]
        def dfs(c, r, location):
            nonlocal used
            flag = False
            # 判断当前字符是否匹配，若不匹配直接返回，剪枝操作
            if board[c][r]==word[location]:
                # 已匹配到最后一个字符且相同，返回True
                if location==l-1: return True
                # 当前字符字符匹配成功，后续递归过程中无法再次使用
                used[c][r] = 1
                # 对当前字符上下左右四个位置中未匹配的字符进行递归
                for dx, dy in bias:
                    x, y = c+dx, r+dy
                    if 0<=x<m and 0<=y<n and not used[x][y]:
                        flag = flag or dfs(x, y, location+1)
                # 回溯状态返回， 此字符可再次被使用. 重点
                used[c][r] = 0
            return flag
        # 遍历二维网格中的每一个字符
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False


board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
board=[["a","a"]]
a = Solution().exist(board, 'aaa')
print(a)
