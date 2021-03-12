#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 =0
        l1 = len(version1)
        l2 = len(version2)
        while p1<l1 and p2 <l2:
            if version1[p1] == '0':
                p1+=1
                continue
            if version2[p2] == '0':
                p2+=1
                continue
            if version1[p1] == version2[p2]:
                p1 +=1
                p2 +=1
                continue
            if version1[p1] == '.' or version2[p2] == '.':
                return -1 if version1[p1] == '.' else 1
            if version1[p1] < version2[p2]:
                return -1
            elif version1[p1] > version2[p2]:
                return 1
        if p1 == l1 and p2 == l2:return 0
        if p1 == l1 and :return -1
        if p2 == l2:return 1

a=Solution().compareVersion(version1 = "1.0.1", version2 = "1")
print(a)