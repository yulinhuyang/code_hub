## 题目描述

```
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

```


// 单链表节点
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) { }
};




// LeetCode, Add Two Numbers
// 跟Add Binary 很类似
// 时间复杂度O(m+n)，空间复杂度O(1)
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode dummy(-1); // 头节点
        int carry = 0;
        ListNode *prev = &dummy;
        for (ListNode *pa = l1, *pb = l2;
             pa != nullptr || pb != nullptr;
             pa = pa == nullptr ? nullptr : pa->next,
             pb = pb == nullptr ? nullptr : pb->next,
             prev = prev->next) {
            const int ai = pa == nullptr ? 0 : pa->val;
            const int bi = pb == nullptr ? 0 : pb->val;
            const int value = (ai + bi + carry) % 10;
            carry = (ai + bi + carry) / 10;
            prev->next = new ListNode(value); // 尾插法
        }
        if (carry > 0)
            prev->next = new ListNode(carry);
        return dummy.next;
    }
};


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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ret = nullptr;
        ListNode* cur = nullptr;
        int carry = 0;
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            carry += (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val);
            auto temp = new ListNode(carry % 10);
            carry /= 10;
            if (ret == nullptr) {
                ret = temp;
                cur = ret;
            }
            else {
                cur->next = temp;
                cur = cur->next;
            }
            l1 = l1 == nullptr ? nullptr : l1->next;
            l2 = l2 == nullptr ? nullptr : l2->next;
        }
        return ret;
    }
};



//递归法
### 算法

1. 将两个链表的第一个节点值相加，结果转为 0-10 之间的个位数，并设置进位信息
2. 将两个链表第一个节点以后的链表做带进位的递归相加
3. 将第一步得到的头节点的 next 指向第二步返回的链表

### C++实现

```C++
// 普通递归
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addTwoNumbers(l1, l2, 0);
    }

private:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, int carry) {
        if (l1 == nullptr && l2 == nullptr && carry == 0) return nullptr;
        carry += (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val);
        auto ret = new ListNode(carry % 10);
        ret->next = addTwoNumbers(l1 == nullptr ? l1 : l1->next,
                                 l2 == nullptr ? l2 : l2->next,
                                 carry / 10);
        return ret;
    }
};
// 类似尾递归
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = nullptr;
        addTwoNumbers(head, nullptr, l1, l2, 0);
        return head;
    }

private:
    void addTwoNumbers(ListNode*& head, ListNode* cur, ListNode* l1, ListNode* l2, int carry) {
        if (l1 == nullptr && l2 == nullptr && carry == 0) return;
        carry += (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val);
        auto temp = new ListNode(carry % 10);
        if (cur == nullptr) {
            head = temp;
            cur = head;
        } else {
            cur->next = temp;
            cur = cur->next;
        }
        addTwoNumbers(head, cur, l1 == nullptr ? l1 : l1->next, l2 == nullptr ? l2 : l2->next, carry / 10);
    }
};