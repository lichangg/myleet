#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 又是一个本地通过网站不过的例子
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCB"

class Solution:
    flag = False

    def exist(self, board, word: str) -> bool:
        hashmap = {}
        m_max = len(board)
        n_max = len(board[0])
        for index_i, i in enumerate(board):
            for index_j, j in enumerate(i):
                if hashmap.get(j):
                    hashmap[j].append((index_i, index_j))
                else:
                    hashmap[j] = [(index_i, index_j)]

        def dp(coordinate, index,cur_used):
            cur_used.append(coordinate)
            if index == len(word):
                Solution.flag = True
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
            together_set = set(coordinate) & set(prob_coordinate)
            for used in cur_used:
                if used in together_set:
                    together_set.remove(used)
            if together_set:
                for i in together_set:
                    dp(i, index + 1, cur_used[:])

        if not hashmap.get(word[0]):
            return False

        for coordinate in hashmap.get(word[0]):
            cur_used = []
            dp(coordinate,1,cur_used)

        return Solution.flag

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]
         ]
a = Solution().exist(board, 'ABCB')
print(a)
