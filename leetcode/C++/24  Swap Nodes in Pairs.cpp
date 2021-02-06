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

## 关键点解析

1. 链表这种数据结构的特点和使用

2. dummyHead 简化操作


// LeetCode, Swap Nodes in Pairs
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode dummy(-1);
        dummy.next = head;

        for(ListNode *prev = &dummy, *cur = prev->next, *next = cur->next;
                next;
                prev = cur, cur = cur->next, next = cur ? cur->next: nullptr) {
            prev->next = next;
            cur->next = next->next;
            next->next = cur;
        }
        return dummy.next;
    }
};



// LeetCode, Swap Nodes in Pairs
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* p = head;

        while (p && p->next) {
            swap(p->val, p->next->val);
            p = p->next->next;
        }

        return head;
    }
};


//azl

CPP Code:

```cpp
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode h, *tail = &h;
        while (head && head->next) {
            auto p = head, q = head->next;
            head = q->next;
            q->next = p;
            tail->next = q;
            tail = p;
        }
        tail->next = head;
        return h.next;
    }
};
```