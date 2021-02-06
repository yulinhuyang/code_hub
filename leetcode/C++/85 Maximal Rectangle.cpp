## 题目描述

给定一个仅包含  0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例：

输入：

```
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```

输出：6

## 前置知识

- 单调栈

// LeetCode, Maximal Rectangle
// 时间复杂度O(n^2)，空间复杂度O(n)
class Solution {
public:
    int maximalRectangle(vector<vector<char> > &matrix) {
        if (matrix.empty())  return 0;

        const int m = matrix.size();
        const int n = matrix[0].size();
        vector<int> H(n, 0);
        vector<int> L(n, 0);
        vector<int> R(n, n);

        int ret = 0;
        for (int i = 0; i < m; ++i) {
            int left = 0, right = n;
            // calculate L(i, j) from left to right
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == '1') {
                    ++H[j];
                    L[j] = max(L[j], left);
                } else {
                    left = j+1;
                    H[j] = 0; L[j] = 0; R[j] = n;
                }
            }
            // calculate R(i, j) from right to left
            for (int j = n-1; j >= 0; --j) {
                if (matrix[i][j] == '1') {
                    R[j] = min(R[j], right);
                    ret = max(ret, H[j]*(R[j]-L[j]));
                } else {
                    right = j;
                }
            }
        }
        return ret;
    }
};




//azl
CPP Code:

```cpp
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& A) {
        if (A.empty() || A[0].empty()) return 0;
        int ans = 0, M = A.size(), N = A[0].size();
        vector<int> left(N, 0), right(N, N), height(N, 0);
        for (int i = 0; i < M; ++i) {
            int curLeft = 0, curRight = N;
            for (int j = 0; j < N; ++j) height[j] = A[i][j] == '1' ? height[j] + 1 : 0;
            for (int j = 0; j < N; ++j) {
                if (A[i][j] == '1') left[j] = max(left[j], curLeft);
                else {
                    left[j] = 0;
                    curLeft = j + 1;
                }
            }
            for (int j = N - 1; j >= 0; --j) {
                if (A[i][j] == '1') right[j] = min(right[j], curRight);
                else {
                    right[j] = N;
                    curRight = j;
                }
            }
            for (int j = 0; j < N; ++j) ans = max(ans, (right[j] - left[j]) * height[j]);
        }
        return ans;
    }
};
```