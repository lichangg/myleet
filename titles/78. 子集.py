#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 执行用时：48 ms, 在所有 Python3 提交中击败了23.98%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了55.74%的用户
# 直接用树的深度搜索解决
class Solution:
    def subsets(self, nums):
        res = [[]]
        def dp(nums,begin_index,path):
            for index in range(begin_index,len(nums)):
                cur_path = path + [nums[index]]
                res.append(cur_path)
                dp(nums,index+1,cur_path[:])

        dp(nums,0,[])
        return res


a=Solution().subsets( [1,2,3])
print(a)