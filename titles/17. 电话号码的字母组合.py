#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 虽然只是看过递归+动态规划的解题思路,但是看到这题的瞬间我就想到了
# 执行用时：36 ms, 在所有 Python3 提交中击败了86.87%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了81.95%的用户
hashmap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        if len(digits)==1:
            return list(hashmap[digits])

        str1=self.letterCombinations(digits[0])
        str2=self.letterCombinations(digits[1:])
        res = []
        for i in str1:
            for j in str2:
                res.append(i+j)
        return res

a=Solution().letterCombinations('23')
print(a)