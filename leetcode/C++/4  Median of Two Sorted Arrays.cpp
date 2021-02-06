## 题目描述

```
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

```

## 前置知识

- 中位数
- 分治法
- 二分查找





// LeetCode, Median of Two Sorted Arrays
// 时间复杂度O(log(m+n))，空间复杂度O(log(m+n))
class Solution {
public:
    double findMedianSortedArrays(const vector<int>& A, const vector<int>& B) {
        const int m = A.size();
        const int n = B.size();
        int total = m + n;
        if (total & 0x1)
            return find_kth(A.begin(), m, B.begin(), n, total / 2 + 1);
        else
            return (find_kth(A.begin(), m, B.begin(), n, total / 2)
                    + find_kth(A.begin(), m, B.begin(), n, total / 2 + 1)) / 2.0;
    }
private:
    static int find_kth(std::vector<int>::const_iterator A, int m, 
            std::vector<int>::const_iterator B, int n, int k) {
        //always assume that m is equal or smaller than n
        if (m > n) return find_kth(B, n, A, m, k);
        if (m == 0) return *(B + k - 1);
        if (k == 1) return min(*A, *B);

        //divide k into two parts
        int ia = min(k / 2, m), ib = k - ia;
        if (*(A + ia - 1) < *(B + ib - 1))
            return find_kth(A + ia, m - ia, B, n, k - ia);
        else if (*(A + ia - 1) > *(B + ib - 1))
            return find_kth(A, m, B + ib, n - ib, k - ib);
        else
            return A[ia - 1];
    }
};


//azl

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) swap(nums1, nums2);
        int M = nums1.size(), N = nums2.size(), L = 0, R = M, K = (M + N + 1) / 2;
        while (true) {
            int i = (L + R) / 2, j = K - i;
            if (i < M && nums2[j - 1] > nums1[i]) L = i + 1;
            else if (i > L && nums1[i - 1] > nums2[j]) R = i - 1;
            else {
                int maxLeft = max(i ? nums1[i - 1] : INT_MIN, j ? nums2[j - 1] : INT_MIN);
                if ((M + N) % 2) return maxLeft;
                int minRight = min(i == M ? INT_MAX : nums1[i], j == N ? INT_MAX : nums2[j]);
                return (maxLeft + minRight) / 2.0;
            }
        }
    }
};