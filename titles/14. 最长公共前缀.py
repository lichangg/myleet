#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 执行用时：48 ms, 在所有 Python3 提交中击败了35.94%的用户
# 内存消耗：13.5 MB, 在所有 Python3 提交中击败了97.63%的用户
# class Solution:
#     def longestCommonPrefix(self, strs) -> str:
#         if not strs:
#             return ''
#         prefix = strs[0]
#         for i in strs[1:]:
#             start = 0
#
#             while start < len(prefix) and start < len(i):
#                 if prefix[start] != i[start]:
#
#                     break
#                 start += 1
#             # 只要循环出来了就需要记录一下当前公共前缀
#             prefix = prefix[0:start]
#
#         return prefix

#执行用时：48 ms, 在所有 Python3 提交中击败了35.94%的用户
#内存消耗：13.8 MB, 在所有 Python3 提交中击败了29.86%的用户
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpRight[:minLength] # 取lcpLeft的切片也行

        return "" if not strs else lcp(0, len(strs) - 1)



a=Solution().longestCommonPrefix(["flower","flow","floght"])
print(a)

