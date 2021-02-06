## 题目描述

```
编写一个程序，找到两个单链表相交的起始节点。
```

## 前置知识

- 链表
- 双指针

## 解法一: 哈希法

有 A, B 这两条链表, 先遍历其中一个，比如 A 链表, 并将 A 中的所有节点存入哈希表。

遍历 B 链表,检查节点是否在哈希表中, 第一个存在的就是相交节点

## 解法二：双指针

- 例如使用 a, b 两个指针分别指向 A, B 这两条链表, 两个指针相同的速度向后移动,
- 当 a 到达链表的尾部时,重定位到链表 B 的头结点
- 当 b 到达链表的尾部时,重定位到链表 A 的头结点。
- a, b 指针相遇的点为相交的起始节点，否则没有相交点


Python Code：

```py
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```