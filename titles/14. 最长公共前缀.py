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
from typing import List


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

# 自己写的
class Solution:
    def get_common(self,s1,s2):
        i,j = 0, 0
        n1 = len(s1)
        n2 = len(s2)
        common = ''
        while i<n1 and j<n2 and s1[i] == s2[j]:
            common += s1[i]
            i+=1
            j+=1
        return common
    def longestCommonPrefix(self, strs) -> str:
        i = 1
        if not strs:
            return ''
        cur_prefix = strs[0]
        while i < len(strs):
            cur_prefix = self.get_common(cur_prefix, strs[i])
            if not cur_prefix:
                return ''
            i+=1
        return cur_prefix

# 这是个取巧的办法的， 找出最长和最短的，其公共前缀就是整个数组字符串的公共前缀（为啥不是最短的和次短的）
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0


a=Solution().longestCommonPrefix(["csa","cd","cs"])
print(a)

