## 题目描述

```
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点  (i, ai) 。在坐标内画 n 条垂直线，垂直线 i  的两个端点分别为  (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与  x  轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且  n  的值至少为 2。

![11.container-with-most-water-question](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu4wyztmj30m90anwep.jpg)

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为  49。



示例：
`
输入：[1,8,6,2,5,4,8,3,7]
输出：49
```

## 前置知识

- 双指针

// LeetCode, Container With Most Water
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    int maxArea(vector<int> &height) {
        int start = 0;
        int end = height.size() - 1;
        int result = INT_MIN;
        while (start < end) {
            int area = min(height[end], height[start]) * (end - start);
            result = max(result, area);
            if (height[start] <= height[end]) {
                start++;
            } else {
                end--;
            }
        }
        return result;
    }
};


//azl   双指针

```C++
class Solution {
public:
    int maxArea(vector<int>& height) {
        auto ret = 0ul, leftPos = 0ul, rightPos = height.size() - 1;
        while( leftPos < rightPos)
        {
            ret = std::max(ret, std::min(height[leftPos], height[rightPos]) * (rightPos - leftPos));
            if (height[leftPos] < height[rightPos]) ++leftPos;
            else --rightPos;
        }
        return ret;
    }
};
```