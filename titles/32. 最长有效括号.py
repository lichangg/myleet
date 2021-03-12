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

# 我怎么都想不明白为啥初始值是-1,二刷的时候明白了
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

# 这个好理解一点, 因为找的条件是需要连续合法,长度都是当前括号的索引减最后那个不符合的括号的索引
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = []
        ans = 0
        for i in range(len(s)):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)  # 下标入栈
            else:
                # 计算结果
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans

# 二刷,思路和上面的一样, 刚开始想着假如队列里面入的都是索引岂不是不知道它到底是'('还是')'了?真是蠢啊,存的是索引,直接按照索引在s里面读不就得到了
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for index, i in enumerate(s):
            if not stack or s[stack[-1]] == ')':
                stack.append(index)
                continue
            if i == '(':
                stack.append(index)
            else:
                if s[stack[-1]] == '(':
                    stack.pop()
                    # 这个else -1 相当的精髓!学到了
                    ans = max(ans, index - (stack[-1] if stack else -1))

        return ans

# 动态规划也可以解决这一题, 不过比栈费劲想一些
# 参考这个: https://leetcode-cn.com/problems/longest-valid-parentheses/solution/dong-tai-gui-hua-si-lu-xiang-jie-c-by-zhanganan042/
# 最重要的是要定义动态规划数组的意义
# 设dp 数组，其中第 i 个元素表示以下标为 i 的字符[结尾!]的[最长有效!]子字符串的长度。 (这句话需要仔细理解)

# 再刷
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        self.max = 0
        for idx, i in enumerate(s):
            if i == '(':
                stack.append(idx)
            else:
                if stack[-1] != -1 and s[stack[-1]] == '(':
                    stack.pop()
                    self.max = max(self.max, idx - stack[-1])
                else:
                    stack.append(idx)

        return self.max
a = Solution().longestValidParentheses('))')
print(a)
