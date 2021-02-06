## 题目描述

```
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

```

## 前置知识

- 链表



def reverseBetween(self, head, m, n):
    if not head or n == m: return head
    p = dummy = ListNode(0)
    dummy.next = head
    for _ in range(m - 1):
        p = p.next
    tail = p.next
    
    for _ in range(n - m):
        temp = p.next
        p.next = tail.next
        tail.next = tail.next.next
        p.next.next = temp
    return dummy.next


//azl
## 关键点解析

- 四点法
- 链表的基本操作
- 考虑特殊情况 m 是 1 或者 n 是链表长度的情况，我们可以采用虚拟节点 dummy 简化操作
- 用四个变量记录特殊节点， 然后操作这四个节点使之按照一定方式连接即可。
- 注意更新 current 和 pre 的位置， 否则有可能出现溢出

## 代码

我把这个方法称为 `四点法`

Python Code:

```Python

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head.next or n == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = None
        cur = head
        i = 0
        p1 = p2 = p3 = p4 = None
        while cur:
            i += 1
            next = cur.next
            if m < i <= n:
                cur.next = pre
            if i == m - 1:
                p1 = cur
            if i == m:
                p2 = cur
            if i == n:
                p3 = cur
            if i == n + 1:
                p4 = cur
            pre = cur
            cur = next
        if not p1:
            dummy.next = p3
        else:
            p1.next = p3
        p2.next = p4
        return dummy.next
```
