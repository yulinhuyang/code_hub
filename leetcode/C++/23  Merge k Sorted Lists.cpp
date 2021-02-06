## 题目描述

```

合并  k  个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

```

## 前置知识

- 链表
- 归并排序

//LeetCode, Merge k Sorted Lists
// 时间复杂度O(n1+n2+...)，空间复杂度O(1)
class Solution {
public:

    ListNode * mergeTwo(ListNode * l1, ListNode * l2){
        if(!l1) return l2;
        if(!l2) return l1;
        ListNode dummy(-1);
        ListNode * p = &dummy;
        for(; l1 && l2; p = p->next){
            if(l1->val > l2->val){
                p->next = l2; l2 = l2->next;
            }
            else{
                p->next = l1; l1 = l1->next;
            }
        }
        p->next = l1 ? l1 : l2;
        return dummy.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) return nullptr;

        // multi pass
        deque<ListNode *> dq(lists.begin(), lists.end());
        while(dq.size() > 1){
            ListNode * first = dq.front(); dq.pop_front();
            ListNode * second = dq.front(); dq.pop_front();
            dq.push_back(mergeTwo(first,second));
        }

        return dq.front();
    }
};


//AZL

```cpp
class Solution {
private:
    ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
        ListNode head(0), *tail = &head;
        while (a && b) {
            if (a->val < b->val) { tail->next = a; a = a->next; }
            else { tail->next = b; b = b->next; }
            tail = tail->next;
        }
        tail->next = a ? a : b;
        return head.next;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return NULL;
        for (int N = lists.size(); N > 1; N = (N + 1) / 2) {
            for (int i = 0; i < N / 2; ++i) {
                lists[i] = mergeTwoLists(lists[i], lists[N - 1 - i]);
            }
        }
        return lists[0];
    }
};
```

