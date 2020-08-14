#!/usr/bin/env python
# -*- coding:utf-8 -*-
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack = ['']
#         max_len = 0
#         cur_len = 0
#
#         for i in s:
#             if i == ')':
#                 if stack[-1] == '(':
#                     cur_len+=2
#                     max_len = max(max_len,cur_len)
#                     stack.pop()
#                 else:
#                     stack.append(i)
#                     cur_len=0
#             if i == '(':
#                 pre = cur_len
#                 stack.append(i)
#
#         return max_len

#我怎么都想不明白为啥初始值是-1
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         ans=0       # 最大合法长度(返回值)
#         stack=[-1,]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
#         for i,ch in enumerate(s):
#             if '('==ch:  # 左括号
#                 stack.append(i)
#             elif len(stack)>1:  # 右括号，且有成对左括号
#                 stack.pop()     # 成对匹配
#                 ans = max(ans, i - stack[-1])
#             else:   # 非法的右括号
#                 stack[0]=i
#         return ans

#这个好理解一点, 因为找的条件是需要连续合法,长度都是当前括号的索引减最后那个不符合的括号的索引
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = []
        ans = 0
        for i in range(len(s)):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)     # 下标入栈
            else:
                # 计算结果
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans

a=Solution().longestValidParentheses('))()(())')
print(a)