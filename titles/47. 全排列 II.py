#!/usr/bin/env python
# -*- coding:utf-8 -*-
#虽然同时记录索引path和数据path是不太方便,
# 但是可以用一个临时变量保存当前index_path（存索引）的相邻左兄弟节点（num_path）[此处能够只用相邻兄弟节点保存的重要前提就是数组是有序的，如果无序的话就得保存先前所有左兄弟节点进行对比了]
# , 通过对比当前num_path和左兄弟节点的num_path是否一致来决定要不要对当前path进行剪枝,
# leetcode网站上没通过[1,2]这个用例，但是本地跑是没问题的
class Solution:
    temp = []
    def permuteUnique(self, nums):
        res = []
        # 重要前提是排序后的
        nums.sort()
        def dfs(nums, res,path, num_index):
            path.append(num_index)
            if Solution.temp == [nums[i] for i in path]:
                return
            if len(path) == len(nums):
                res.append([nums[i] for i in path])
                return
            for index in range(len(nums)):
                if index in path:
                    continue
                dfs(nums,res,path[:],index)
            Solution.temp = [nums[i] for i in path]
        for index,i in enumerate(nums):
            dfs(nums,res,[],index)
        return res

# 别人的，有空记得看
# from typing import List
#
#
# class Solution:
#
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#
#         def dfs(nums, size, depth, path, used, res):
#             if depth == size:
#                 res.append(path.copy())
#                 return
#             for i in range(size):
#                 if not used[i]:
#
#                     if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
#                         continue
#
#                     used[i] = True
#                     path.append(nums[i])
#                     dfs(nums, size, depth + 1, path, used, res)
#                     used[i] = False
#                     path.pop()
#
#         size = len(nums)
#         if size == 0:
#             return []
#
#         nums.sort()
#
#         used = [False] * len(nums)
#         res = []
#         dfs(nums, size, 0, [], used, res)
#         return res

a=Solution().permuteUnique([1,2,1,2])
print(a)
