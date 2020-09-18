#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
# 当n为3,也就是数的值为[1,2,3]的时候
# 如果提起1作为树根，左边有f(0)种情况，右边f(2)种情况，左右搭配一共有f(0)*f(2)种情况
# 如果提起2作为树根，左边有f(1)种情况，右边f(1)种情况，左右搭配一共有f(1)*f(1)种情况
# 如果提起3作为树根，左边有f(2)种情况，右边f(0)种情况，左右搭配一共有f(2)*f(0)种情况
# 容易得知f(3) = f(0)*f(2) + f(1)*f(1) + f(2)*f(0)
# 同理,
# f(4) = f(0)*f(3) + f(1)*f(2) + f(2)*f(1) + f(3)*f(0)
# f(5) = f(0)*f(4) + f(1)*f(3) + f(2)*f(2) + f(3)*f(1) + f(4)*f(0)
# 对于每一个n，其式子都是有规律的
# 每一项两个f()的数字加起来都等于n-1
class Solution:
    def numTrees(self, n: int) -> int:
        nums= [1,1,2]
        for m in range(3,n+1):
            s = m - 1
            count = 0
            for i in range(m):
                count += nums[i] * nums[s - i]
            nums.append(count)
        return nums[-1]

# 二刷失败
a=Solution().numTrees(3)
print(a)