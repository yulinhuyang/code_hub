题目描述
``` 给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix = [ [1,2,3], [4,5,6], [7,8,9] ],
原地旋转输入矩阵，使其变为: [ [7,4,1], [8,5,2], [9,6,3] ] 示例 2:
给定 matrix = [ [ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16] ],
原地旋转输入矩阵，使其变为: [ [15,13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7,10,11] ]



// LeetCode, Rotate Image
// 思路 1，时间复杂度O(n^2)，空间复杂度O(1)
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int n = matrix.size();

        for (int i = 0; i < n; ++i)  // 沿着副对角线反转
            for (int j = 0; j < n - i; ++j)
                swap(matrix[i][j], matrix[n - 1 - j][n - 1 - i]);

        for (int i = 0; i < n / 2; ++i) // 沿着水平中线反转
            for (int j = 0; j < n; ++j)
                swap(matrix[i][j], matrix[n - 1 - i][j]);
    }
};




// LeetCode, Rotate Image
// 思路 2，时间复杂度O(n^2)，空间复杂度O(1)
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int n = matrix.size();

        for (int i = 0; i < n / 2; ++i) // 沿着水平中线反转
            for (int j = 0; j < n; ++j)
                swap(matrix[i][j], matrix[n - 1 - i][j]);

        for (int i = 0; i < n; ++i)  // 沿着主对角线反转
            for (int j = i + 1; j < n; ++j)
                swap(matrix[i][j], matrix[j][i]);
    }
};



## 关键点解析

- 矩阵旋转操作

//AZL

CPP Code:

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int N = matrix.size();
        for (int i = 0; i < N / 2; ++i) {
            for (int j = i; j < N - i - 1; ++j) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[N - j - 1][i];
                matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1];
                matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1];
                matrix[j][N - i - 1] = tmp;
            }
        }
    }
};
```