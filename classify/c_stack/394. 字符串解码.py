#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路1
# 因为数字后面除了接数字外必跟一个左括号, 所以数字存放在数字栈，字符串存放在字符串栈，
# 1. 遇到右括号时候弹出一个数字栈，同时字母栈弹到左括号为止, 字母和数字运算后压入字母栈
# 2. 遇到数字累计起来, 等遇到左括号时压入数字栈, 同时数字置空
# 3. 遇到左括号当前字符和左括号都压入字母栈, 同时累计的数字压入数字栈
# 4. 最后合并


# 太不优雅了....
class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        digit_stack = []
        c=''
        n = ''
        for i in s:
            if i.isdigit():
                n +=i
            elif i == '[':
                digit_stack.append(int(n))
                n=''
                if c:
                    str_stack.append(c)
                    c=''
                str_stack.append('[')
            elif i == ']':
                digi = digit_stack.pop()
                pre = str_stack.pop()
                while pre != '[':
                    c = pre +c
                    if not str_stack:
                        break
                    pre = str_stack.pop()
                c = digi*c
                str_stack.append(c)
                c=''
            else:
                c+=i

        return ''.join(str_stack) + c

# 思路一优雅的写法
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res]) # 左括号必是数字(题目规定的)
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res # 上一个结果和当前结果乘以数字后的结果相加
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)           # 用一个倍数记录数字,妙啊
            else:
                res += c
        return res

# 思路二:递归:好像也挺简单的, 把[作为递归开始条件, 把]作为终止递归条件
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)

a=Solution().decodeString("10[10[abc]]")
print(a)