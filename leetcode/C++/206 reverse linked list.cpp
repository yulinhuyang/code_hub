
## 题目描述

反转一个单链表。

```
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

```

## 关键点解析

- 链表的基本操作（交换）
- 虚拟节点 dummy 简化操作
- 注意更新 current 和 pre 的位置， 否则有可能出现溢出

## 代码

//azl
C++ Code：

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* cur = head;
        ListNode* next = NULL;
        while (cur != NULL) {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
};
```

递归
C++实现

```c++
// 普通递归
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* tail = nullptr;
        return reverseRecursive(head, tail);
    }

    ListNode* reverseRecursive(ListNode *head, ListNode *&tail) {
        if (head == nullptr) {
            tail = nullptr;
            return head;
        }
        if (head->next == nullptr) {
            tail = head;
            return head;
        }
        auto h = reverseRecursive(head->next, tail);
        if (tail != nullptr) {
            tail->next = head;
            tail = head;
            head->next = nullptr;
        }
        return h;
    }
};

// （类似）尾递归
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return head;
        return reverseRecursive(nullptr, head, head->next);
    }

    ListNode* reverseRecursive(ListNode *prev, ListNode *head, ListNode *next)
    {
        if (next == nullptr) return head;
        auto n = next->next;
        next->next = head;
        head->next = prev;
        return reverseRecursive(head, next, n);
    }
};