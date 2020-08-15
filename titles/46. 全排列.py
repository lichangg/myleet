#!/usr/bin/env python
# -*- coding:utf-8 -*-
#深度递归搜索， path记录的是数据
# class Solution:
#
#     def permute(self, nums):
#         res = []
#         def dfs(nums, res,path, num_index):
#             path.append(nums[num_index])
#             if len(path) == len(nums):
#                 res.append(path)
#                 return
#             for index in range(len(nums)):
#                 # 只有不在path里面的值可以被添加
#                 if nums[index] in path:
#                     continue
#                 # 这里一定要注意是将path[:],如果把path本尊传过去会导致它会被别的分支一直改动！！！
#                 dfs(nums,res,path[:],index)
#         for index,i in enumerate(nums):
#             dfs(nums,res,[],index)
#         return res

#深度递归搜索， path记录的是数据在原数组中的索引，效率同上
class Solution:
    def permute(self, nums):
        res = []
        def dfs(nums, res,path, num_index):
            path.append(num_index)
            if len(path) == len(nums):
                res.append([nums[i] for i in path])
                return
            for index in range(len(nums)):
                if index in path:
                    continue
                dfs(nums,res,path[:],index)
        for index,i in enumerate(nums):
            dfs(nums,res,[],index)
        return res
a=Solution().permute([1,2,4])
print(a)