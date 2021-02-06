
```
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

```

## 前置知识

- 链表
- 栈


## 关键点解析

- 栈的基本操作
- carried 变量记录进位
- 循环的终止条件设置成`stack.length > 0` 可以简化操作
- 注意特殊情况， 比如 1 + 99 = 100


C++ Code：

```C++
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
        auto carry = 0;
        auto ret = (ListNode*)nullptr;
        auto s1 = vector<int>();
        toStack(l1, s1);
        auto s2 = vector<int>();
        toStack(l2, s2);
        while (!s1.empty() || !s2.empty() || carry != 0) {
            auto v1 = 0;
            auto v2 = 0;
            if (!s1.empty()) {
                v1 = s1.back();
                s1.pop_back();
            }
            if (!s2.empty()) {
                v2 = s2.back();
                s2.pop_back();
            }
            auto v = v1 + v2 + carry;
            carry = v / 10;
            auto tmp = new ListNode(v % 10);
            tmp->next = ret;
            ret = tmp;
        }
        return ret;
    }
private:
    // 此处若返回而非传入vector，跑完所有测试用例多花8ms
    void toStack(const ListNode* l, vector<int>& ret) {
        while (l != nullptr) {
            ret.push_back(l->val);
            l = l->next;
        }
    }
};

// 逆置，相加，再逆置。跑完所有测试用例比第一种解法少花4ms
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto rl1 = reverseList(l1);
        auto rl2 = reverseList(l2);
        auto ret = add(rl1, rl2);
        return reverseList(ret);
    }
private:
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

    ListNode* add(ListNode* l1, ListNode* l2) {
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
```

