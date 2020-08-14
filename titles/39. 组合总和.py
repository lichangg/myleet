#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 深度优先搜索
class Solution:
    def combinationSum(self, candidates, target: int):
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝是为了提速，在本题非必需
        candidates.sort()
        # 在遍历的过程中记录路径，它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
            return
        # 从begin开始可以去除重复的组合, [for是一个当前节点产子节点的过程, 当被break后不再产后面的弟弟子节点, 越往下越容易被break出来]
        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 如果不从当前index而是从0开始的话会出现重复分支[注意!这个剪枝操作一定要先将nums排序]
            self.__dfs(candidates, index, size, path, res, residue)
            # 回溯,将最后一个元素删除
            path.pop()

#这个以后再看
# class Solution:
#     def combinationSum(self, candidates, target: int):
#         res = []
#         def func(nums, target, vis):
#             # 终止条件
#             if target==0: # 刚好加起来等于target
#                 res.append(vis)
#                 return
#             if target<0: # 无法满足此target
#                 return
#
#             # 递归调用
#             for i, ele in enumerate(nums):
#                 func(nums[i:], target-ele, vis+[ele]) # nums[i:]保证了不会取到重复的组合
#
#         func(candidates, target, [])
#         return res
a=Solution().combinationSum([8,7,4,3],11)
print(a)