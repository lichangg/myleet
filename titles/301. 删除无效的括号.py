#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 自己写的
# 思路就是分为多了左括号和右括号的情况
# 1. 多左括号,删多余的左括号,返回的结果里面只有一种情况
# 2. 多右括号:
#   1.只多一个, 遍历删除索引小于[该多余的右括号的索引]的右括号,
#   2.多余N个, 排列组合删除N个,删除对象是索引小于[最大多余括号索引]的右括号
# 不知道对不对

# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         s= list(s)
#         stack = []
#         remove_l = []
#         remove_r = []
#         for index, i in enumerate(s):
#             if i == ')':
#                 if not stack:
#                    remove_r.append(index)
#                 else:
#                     stack.pop()
#                     remove_l.pop()
#             elif i =='(':
#                 stack.append(index)
#                 remove_l.append(index)
#             else:
#                 pass
#         if remove_l:
#             only_s=''
#             # 学到了, 批量删除指定索引的方法
#             for index, i in enumerate(s):
#                 if index not in remove_l:
#                     only_s+=i
#             return [only_s]
#         else:
#
#             s1=[]
#             remove_count = len(remove_r)
#             max_remove = max(remove_r)
#             count =
#             for index, i in enumerate(s):
#                 if index>max_remove or count==remove_count:
#                     break
#                 if i == ')':

# BFS很简单,复杂度为O(2^N)
# 思路就是以完整字符串为根,依次删除每个括号得到子节点组成下一层, 依次类推,[注意:每层都需要去重],得到合法的字符串集合就返回
class Solution:
    def removeInvalidParentheses(self, s:str) -> List[str]:
        # 验证是否合法的方法
        def isValid(s:str)->bool:
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level

#二刷失败, 上述算法核心就是BFS, 很好理解, 学到了

a=Solution().removeInvalidParentheses(')))(a)(()())')
print(a)

