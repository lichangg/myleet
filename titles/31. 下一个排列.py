#!/usr/bin/env python
# -*- coding:utf-8 -*-
#这种方法始终会用到额外空间,而题目要求[原地]修改
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def get_str_list(s):
            if len(s) == 1:
                return s
            head = s[0]
            sub = s[1:]
            if sub==sorted(sub,reverse=True):
                if s == sorted(s,reverse=True):
                    return sorted(s)
                for index,i in enumerate(sub):
                    if (index+1==len(sub) and i > head) or s[index+1] < head:
                        s[0], s[index+1] = s[index+1], s[0]
                        sub=sorted(s[1:])
                        sub.insert(0,s[0])
                        return sub
                else:
                    return sorted(s)
            else:
                sub = get_str_list(sub)
                sub.insert(0, head)
                return sub
        nums = get_str_list(nums)
        print(nums)

Solution().nextPermutation([1,2,3])


