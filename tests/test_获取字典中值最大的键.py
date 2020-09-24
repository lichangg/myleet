#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 该方法有个缺陷就是只能返回第一个最大的, 之后的还有最大的就不管了
a={'A':1,'B':2,'D':3,'C':3}

n=max(a,key=a.get)
print(n)
