#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 执行用时：44 ms, 在所有 Python3 提交中击败了55.94%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了63.38%的用户
# class Solution:
#     def isValid(self, s: str) -> bool:
#         hashmap = {'(':')','{':'}','[':']'}
#         stack = []
#
#         for i in s:
#             if i not in hashmap :
#                 if not stack:
#                     return False
#                 if hashmap[stack[-1]] != i:
#                     return False
#                 else:
#                     stack.pop()
#             else:
#                 stack.append(i)
#
#         if stack:
#             return False
#         else:
#             return True

# 别人写的简单一点
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False
        return len(stack) == 1

a=Solution().isValid('[()[]]')
print(a)