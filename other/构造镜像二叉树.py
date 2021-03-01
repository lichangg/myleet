#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import create_BTree_By_List
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return
        if not pRoot.left and not pRoot.right:
            return pRoot
        # 此处一定要注意, 下面这个综合的赋值语句千万不能拆成两句了写,因为例如先赋值了left,原left被覆盖掉了, 而right的生成是需要源left的!!!
        pRoot.left,  pRoot.right= self.Mirror(pRoot.right),self.Mirror(pRoot.left)

        return pRoot
a=create_BTree_By_List([8,6,10,5,7,9,11])
a=Solution().Mirror(a)
print(a)
