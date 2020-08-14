#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 投机取巧, 没啥意义
# 执行用时：64 ms, 在所有 Python3 提交中击败了12.31%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了76.31%的用
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0
#
#         le = len(needle)
#         for index,i in enumerate(haystack):
#             if needle == haystack[index:index+le]:
#                 return index
#         else:
#             return -1

#KMP算法超时
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for index, s in enumerate(haystack):
            j=0
            offset = 0
            while j<=len(needle) and (offset + index)<len(haystack):
               if haystack[index+offset] == needle[j]:

                   offset+=1
                   j+=1
                   if j == len(needle):
                       return index
               else:
                   break
        else:
            return -1


a=Solution().strStr('a', '')
print(a)