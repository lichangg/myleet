#!/usr/bin/env python
# -*- coding:utf-8 -*-
#其只要了解一点：我们一个一个地排队，对于前面已经排好的队，
# 如果我们在k的位置插入一个新人，那么对k之前的人没有任何影响，对于k之后比新人高的人也没有任何影响，
# 因此，我们每插入一个人的时候，要么保证前面所有人都比新人高，要么至少保证插入的位置后面的所有人都比新人高。
