#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

#这不行
# class Solution:
#     def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
#         tmp = []
#         for pair in adjacentPairs:
#             one = pair[0]
#             two = pair[1]
#
#             if one not in tmp and two not in tmp:
#                 tmp.extend([None, one, two, None])
#             elif one not in tmp:
#                 idx = tmp.index(two)
#                 one_insert_idx = idx-1 if tmp[idx-1] is None else idx + 1
#                 tmp[one_insert_idx] = one
#             elif two not in tmp:
#                 idx = tmp.index(one)
#                 two_insert_idx = idx-1 if tmp[idx-1] is None else idx + 1
#                 tmp[two_insert_idx] = two
#             else:
#
#         return list(filter(None, tmp))
#用双端队列都过不了第39个用例,老超时
from collections import defaultdict
from collections import deque
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        initial_item =adjacentPairs[0][0]
        adjacent_info = defaultdict(list)
        for pair in adjacentPairs:
            adjacent_info[pair[0]].append(pair[1])
            adjacent_info[pair[1]].append(pair[0])
        def dfs(root, tmp, parent):
            if root in tmp:
                return
            if not parent or tmp[0]== parent:
                tmp.appendleft(root)
            else:
                tmp.append(root)
            if len(adjacent_info[root]) == 1:
                dfs(adjacent_info[root][0], tmp, root)
            else:
                adj1, adj2 = adjacent_info[root]
                if not parent:
                    dfs(adj1, tmp, root)
                    dfs(adj2, tmp, root)
                elif adj1 == parent:
                    dfs(adj2, tmp, root)
                else:
                    dfs(adj1, tmp, root)

        path = deque()

        dfs(initial_item, path, None)

        return list(path)
# 用双端对立
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        initial_item =adjacentPairs[0][0]
        adjacent_info = defaultdict(list)
        for pair in adjacentPairs:
            adjacent_info[pair[0]].append(pair[1])
            adjacent_info[pair[1]].append(pair[0])
        def dfs(root, tmp, parent):

            if len(adjacent_info[root]) == 1:
                tmp.appendleft(root)
                return
            else:
                tmp.appendleft(root)
                adj1, adj2 = adjacent_info[root]
                if adj1 == parent:
                    dfs(adj2, tmp, root)
                else:
                    dfs(adj1, tmp, root)

        def dfs2(root, tmp, parent):
            if len(adjacent_info[root]) == 1:
                if parent:
                    tmp.append(root)
                return
            else:
                if parent:
                    tmp.append(root)
                adj2, adj1 = adjacent_info[root]
                if adj1 == parent:
                    dfs2(adj2, tmp, root)
                else:
                    dfs2(adj1, tmp, root)
        path = deque()

        dfs(initial_item, path, None)
        dfs2(initial_item, path, None)
        return list(path)
#这方法还是蛮巧妙的
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        n = len(adjacentPairs) + 1
        for x,y in adjacentPairs:
            dic[x].append(y)
            dic[y].append(x)
        head = [k for k,v in dic.items() if len(v)==1]
        res = [head[0]]
        while len(res) < n:
            i = res[-1]
            j = dic[i].pop()
            dic[j].remove(i)
            res.append(j)
        return res

a=Solution().restoreArray([[4,-2],[1,4],[-3,1]])
print(a)