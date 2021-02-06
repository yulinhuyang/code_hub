
## 题目描述

```
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

```

## 前置知识

- 链表
- 双指针


// LeetCode, Remove Nth Node From End of List
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode dummy{-1, head};
        ListNode *p = &dummy, *q = &dummy;

        for (int i = 0; i < n; i++)  // q先走n步
            q = q->next;

        while(q->next) { // 一起走
            p = p->next;
            q = q->next;
        }
        ListNode *tmp = p->next;
        p->next = p->next->next;
        delete tmp;
        return dummy.next;
    }
};


//AZL 
//双指针

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *p = head, *q = head;
        while (n--) q = q->next;
        if (!q) {
            head = head->next;
            delete p;
            return head;
        }
        while (q->next) p = p->next, q = q->next;
        q = p->next;
        p->next = q->next;
        delete q;
        return head;
    }
};
```