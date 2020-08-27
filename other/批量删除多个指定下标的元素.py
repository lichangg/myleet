#!/usr/bin/env python
# -*- coding:utf-8 -*-\
# 方法1
nums = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'x', 'y']
ans = [0, 3, 7]  # 'a', 'd', 'h'
cnt = 0
for a in ans:
    del nums[a-cnt]
    cnt += 1
print(nums)

# 方法2
output = []
for index, i in enumerate(nums):
    if index not in ans:
        output.append(i)