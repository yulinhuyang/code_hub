## 题目描述

```
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

 

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

```

## 前置知识

- 链表

// LeetCode, Partition List
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode left_dummy(-1); // 头结点
        ListNode right_dummy(-1); // 头结点

        auto left_cur = &left_dummy;
        auto right_cur = &right_dummy;

        for (ListNode *cur = head; cur; cur = cur->next) {
            if (cur->val < x) {
                left_cur->next = cur;
                left_cur = cur;
            } else {
                right_cur->next = cur;
                right_cur = cur;
            }
        }

        left_cur->next = right_dummy.next;
        right_cur->next = nullptr;

        return left_dummy.next;
    }
};



//azl
CPP Code:

```cpp
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode dummy, geHead, *ltTail = &dummy, *geTail = &geHead;
        while (head) {
            auto p = head;
            head = head->next;
            if (p->val < x) {
                ltTail->next = p;
                ltTail = p;
            } else {
                geTail->next = p;
                geTail = p;
            }
        }
        ltTail->next = geHead.next;
        geTail->next = NULL;
        return dummy.next;
    }
};