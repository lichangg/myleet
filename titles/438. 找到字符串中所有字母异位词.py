#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 这种解法遇到s是'aaaaaa...',p是'aaaa....'的时候会超时,本质是遇到不符合要求的字符时不会跳
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for i in p:
            hashmap[i] += 1
        res = []
        for index, i in enumerate(s):
            if i not in hashmap:
                continue
            start = index
            j = 0
            need_hashmap = hashmap.copy()
            count = len(p)
            while start + j < len(s):
                need_hashmap[s[start + j]] -= 1
                if need_hashmap[s[start + j]] >= 0:
                    count -= 1
                    if count == 0:
                        res.append(index)
                        break
                else:
                    break
                j += 1
        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        '''
        解法1：滑动窗口
        '''
        res = []
        window = {}     # 记录窗口中各个字符数量的字典
        needs = {}      # 记录目标字符串中各个字符数量的字典
        for c in p: needs[c] = needs.get(c, 0) + 1  # 统计目标字符串的信息

        length, limit = len(p), len(s)
        left = right = 0                    # 定理两个指针，分别表示窗口的左、右界限

        while right < limit:
            c = s[right]
            if c not in needs:              # 当遇到不需要的字符时
                window.clear()              # 将之前统计的信息全部放弃
                left = right = right + 1    # 从下一位置开始重新统计,[也就是之前解法未解决的跳过]
            else:
                window[c] = window.get(c, 0) + 1            # 统计窗口内各种字符出现的次数
                if right-left+1 == length:                  # 当窗口大小与目标字符串长度一致时
                    if window == needs: res.append(left)    # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    window[s[left]] -= 1                    # 并将移除的字符数量减一
                    left += 1                               # left右移
                right += 1                                  # right右移
        return res


a = Solution().findAnagrams("cbaebabacd", 'abc')
print(a)
