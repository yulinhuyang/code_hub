
## 题目描述

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

![image.png](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

```
示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
```

## 前置知识

- 链表

## 思路

设置一个 dummy 节点简化操作，dummy next 指向 head。

1. 初始化 first 为第一个节点
2. 初始化 second 为第二个节点
3. 初始化 current 为 dummy
4. first.next = second.next
5. second.next = first
6. current.next = second
7. current 移动两格
8. 重复



## 关键点解析

1. 链表这种数据结构的特点和使用

2. dummyHead 简化操作


//azl
Python Code:

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        用递归实现链表相邻互换：
        第一个节点的 next 是第三、第四个节点交换的结果，第二个节点的 next 是第一个节点；
        第三个节点的 next 是第五、第六个节点交换的结果，第四个节点的 next 是第三个节点；
        以此类推
        :param ListNode head
        :return ListNode
        """
        # 如果为 None 或 next 为 None，则直接返回
        if not head or not head.next:
            return head

        _next = head.next
        head.next = self.swapPairs(_next.next)
        _next.next = head
        return _next
```