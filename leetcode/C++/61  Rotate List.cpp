## 题目描述

```
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
```

## 快慢指针法


// LeetCode, Remove Rotate List
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    ListNode *rotateRight(ListNode *head, int k) {
        if (head == nullptr || k == 0) return head;

        int len = 1;
        ListNode* p = head;
        while (p->next) { // 求长度
            len++;
            p = p->next;
        }
        k = len - k % len;

        p->next = head; // 首尾相连
        for(int step = 0; step < k; step++) {
            p = p->next;  //接着往后跑
        }
        head = p->next; // 新的首节点
        p->next = nullptr; // 断开环
        return head;
    }
};


//AZL

### 思路二代码

- 伪代码

```js
  获取链表的长度
  k = k % 链表的长度
  获取倒数第k + 1,倒数第K个节点与链表尾节点
  倒数第k + 1个节点.next = null
  链表尾节点.next = head
  return 倒数第k个节点
```

CPP Code:

```cpp
class Solution {
    int getLength(ListNode *head) {
        int len = 0;
        for (; head; head = head->next, ++len);
        return len;
    }
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return NULL;
        int len = getLength(head);
        k %= len;
        if (k == 0) return head;
        auto p = head, q = head;
        while (k--) q = q->next;
        while (q->next) {
            p = p->next;
            q = q->next;
        }
        auto h = p->next;
        q->next = head;
        p->next = NULL;
        return h;
    }
};
```