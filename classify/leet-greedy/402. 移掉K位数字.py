#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 首先题目可以转为保留的数字最小, 因为要使留下来的数字尽量小, 所以得从高位开始遍历尽量去掉大的数
# 1. 维护一个单调递增栈, 里面存储的都是要保留的数字, 该栈最后的长度得是要保留的数字长度,初始化工作完后开始进入遍历
# 2. 若当前数字比栈顶元素要大则直接加入
# 3. 若当前数字比栈顶元素小则进入循环(因为要准备替代栈顶的那个大元素了), 另外还要注意的是num还剩多少数字可供添加, 若已经不足以填满栈就不用循环了(贪心)
#    - 循环内部也是若剩下的数字不足以填满栈也可以直接跳出(贪心)
# 4. 经过上面步骤后得到栈长度有可能是超出要保留的数字长度的(例如"123456789", 要保留5位), 所以需要裁到保留的长度
# 5. 最后去掉左0
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        k = len(num) - k
        stack = []
        res = ''
        for idx, i in enumerate(num):
            while stack and i < stack[-1] and len(stack) + len(num) - idx> k:
                stack.pop()

            stack.append(i)
            if len(stack) + len(num) - idx - 1 <=k:
                stack += num[idx+1:]
                break
        # 要是循环完保留的数字比k还多那就得裁掉后面的
        res = ''.join(stack[:k])
        res = res.lstrip('0')
        return res or '0'




a=Solution().removeKdigits(num = "112", k = 1)
print(a)