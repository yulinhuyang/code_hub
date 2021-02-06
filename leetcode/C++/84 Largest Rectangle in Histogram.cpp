## 题目描述

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

![](https://tva1.sinaimg.cn/large/007S8ZIlly1ghltx8sr4uj305805odfn.jpg)

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为  [2,1,5,6,2,3]。

![](https://tva1.sinaimg.cn/large/007S8ZIlly1ghltx9kgd2j305805oa9z.jpg)

图中阴影部分为所能勾勒出的最大矩形面积，其面积为  10  个单位。

```
示例：

输入：[2,1,5,6,2,3]
输出：10

```


// LeetCode, Largest Rectangle in Histogram
// 时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        stack<int> s;
        height.push_back(0);
        int result = 0;
        for (int i = 0; i < height.size(); ) {
            if (s.empty() || height[i] > height[s.top()])
                s.push(i++);
            else {
                int tmp = s.top();
                s.pop();
                result = max(result,
                        height[tmp] * (s.empty() ? i : i - s.top() - 1));
            }
        }
        return result;
    }
};


//AZL 单调栈
CPP Code:

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& A) {
        A.push_back(0);
        int N = A.size(), ans = 0;
        stack<int> s;
        for (int i = 0; i < N; ++i) {
            while (s.size() && A[s.top()] >= A[i]) {
                int h = A[s.top()];
                s.pop();
                int j = s.size() ? s.top() : -1;
                ans = max(ans, h * (i - j - 1));
            }
            s.push(i);
        }
        return ans;
    }
};
