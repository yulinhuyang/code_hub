## 题目描述

```
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
```

//归并排序

//LeetCode, Merge Sorted Array
// 时间复杂度O(m+n)，空间复杂度O(1)
class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        int ia = m - 1, ib = n - 1, icur = m + n - 1;
        while(ia >= 0 && ib >= 0) {
            A[icur--] = A[ia] >= B[ib] ? A[ia--] : B[ib--];
        }
        while(ib >= 0) {
            A[icur--] = B[ib--];
        }
    }
};


//azl
C++ code:

```
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int current = m + n - 1;
        while (current >= 0) {
            if (n == 0) return;
            if (m < 1) {
                nums1[current--] = nums2[--n];
                continue;
            }
            if (n < 1) {
                nums1[current--] = nums1[--m];
                continue;
            }
            if (nums1[m - 1] > nums2[n - 1]) nums1[current--] = nums1[--m];
            else nums1[current--] = nums2[--n];
        }
    }
};
```