#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 堆在物理上是一个数组，在逻辑上是一个二叉树。
# 大堆：根结点比孩子结点大；
# 小堆：根结点比孩子结点小；
# 堆化（向下调整）、向上调整的前提都是：在二叉树中，只有一个位置不满足堆的性质，其它位置都满足堆的性质。
# 向下调整 是让调整的结点与其孩子节点进行比较
# 向上调整 是让调整的结点与其父亲结点进行比较
# 已知双亲的下标，则左孩子的下标为：left=2parent+1；
# 则右孩子的下标为：left=2parent+2；
# 已知孩子结点（不区分左右）的下标，则双亲的下标为：（child-1）/2；
class heapq:
    def __init__(self):
        pass

    def heapqify(self, nums):
        """
        构建最小堆
        :param nums:需要调整的数组
        :return:
        """
        for i in range(len(nums) // 2, -1, -1):
            self.__down_adjust(nums, i, len(nums))

    def __down_adjust(self, nums, low, high):
        """
        向下调整
        :param nums:
        :param low:起始节点
        :param high: 需要调整的数组中元素的个数
        :return:
        """
        parent = low
        left = 2 * parent + 1
        while parent < high:
            if left + 1 < high and nums[left + 1] < nums[left]:
                left += 1
            if left < high and nums[left] < nums[parent]:
                nums[parent], nums[left] = nums[left], nums[parent]
                parent = left
                left = 2 * parent + 1
            else:
                break

    def heappop(self, nums):
        """
        将当前最小元素出栈
        将最小元素与数组最后一个元素互换，然后采用向下调整的方式
        :return:
        """
        if len(nums) < 1:
            raise IndexError("超出数组范围！")
        nums[0], nums[-1] = nums[-1], nums[0]
        self.__down_adjust(nums, 0, len(nums) - 1)
        return nums.pop()

    def heappush(self, nums, val):
        """
        插入元素，并采用向上调整的方法
        :param val:
        :return:
        """
        nums.append(val)
        self.__up_adjust(nums, 0, len(nums))

    def __up_adjust(self, nums, low, high):
        """
        向上调整
        :param nums:
        :param low:
        :param high:
        :return:
        """
        child = high - 1
        parent = (child - 1) // 2
        while parent >= low:
            if nums[child] < nums[parent]:
                nums[child], nums[parent] = nums[parent], nums[child]
                child = parent
                parent = child // 2
            else:
                break

    def heapreplace(self, nums, val):
        """
        替换栈顶元素
        :param nums:
        :param val:
        :return:
        """
        returnitem = nums[0]
        nums[0] = val
        self.__down_adjust(nums, 0, len(nums))
        return returnitem

    def heappushpop(self,nums,val):
        if nums and nums[0] < val:
            val, nums[0] = nums[0], val
            self.__down_adjust(nums, 0, len(nums))
        return val

if __name__ == "__main__":
    ex= [8,5,9,4,1,5,7,2,4]
    h = heapq()
    h.heapqify(ex)
    h.heappush(ex, 0)
    h.heappush(ex, -1)
    a=h.heappop(ex)
    print(ex)
    print(a)