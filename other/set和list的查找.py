#!/usr/bin/env python
# -*- coding:utf-8 -*-
a={1,2,3,4,5,6,7,8,9,10}
b=[1,2,3,4,5,6,7,8,9,10]

import time
start_l = time.time()
for i in range(1000000):
    if 11 in a:
        b=1
end_l = time.time()
print(end_l - start_l)

start_s = time.time()
for i in range(1000000):
    if 11 in b:
        b=1
end_s = time.time()
print(end_s - start_s)