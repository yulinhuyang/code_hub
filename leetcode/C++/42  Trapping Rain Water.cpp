
## 题目描述

```
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


```

![42.trapping-rain-water-1](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlu8i4s97j30bg04hmx3.jpg)

```
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

```

## 前置知识

- 空间换时间
- 双指针
- 单调栈



// LeetCode, Trapping Rain Water
// 思路1，时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    int trap(const vector<int>& A) {
        const int n = A.size();
        int *max_left = new int[n]();
        int *max_right = new int[n]();

        for (int i = 1; i < n; i++) {
            max_left[i] = max(max_left[i - 1], A[i - 1]);
            max_right[n - 1 - i] = max(max_right[n - i], A[n - i]);

        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            int height = min(max_left[i], max_right[i]);
            if (height > A[i]) {
                sum += height - A[i];
            }
        }

        delete[] max_left;
        delete[] max_right;
        return sum;
    }
};




// LeetCode, Trapping Rain Water
// 思路2，时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    int trap(const vector<int>& A) {
        const int n = A.size();
        int max = 0; // 最高的柱子，将数组分为两半
        for (int i = 0; i < n; i++)
            if (A[i] > A[max]) max = i;

        int water = 0;
        for (int i = 0, peak = 0; i < max; i++)
            if (A[i] > peak) peak = A[i];
            else water += peak - A[i];
        for (int i = n - 1, top = 0; i > max; i--)
            if (A[i] > top) top = A[i];
            else water += top - A[i];
        return water;
    }
};





// LeetCode, Trapping Rain Water
// 用一个栈辅助，小于栈顶的元素压入，大于等于栈顶就把栈里所有小于或
// 等于当前值的元素全部出栈处理掉，计算面积，最后把当前元素入栈
// 时间复杂度O(n)，空间复杂度O(n)
class Solution {
public:
    int trap(const vector<int>& A) {
        const int n = A.size();
        stack<pair<int, int>> s;
        int water = 0;

        for (int i = 0; i < n; ++i) {
            int height = 0;

            while (!s.empty()) { // 将栈里比当前元素矮或等高的元素全部处理掉
                int bar = s.top().first;
                int pos = s.top().second;
                // bar, height, A[i] 三者夹成的凹陷
                water += (min(bar, A[i]) - height) * (i - pos - 1);
                height = bar;

                if (A[i] < bar) // 碰到了比当前元素高的，跳出循环
                    break;
                else
                    s.pop(); // 弹出栈顶，因为该元素处理完了，不再需要了
            }

            s.push(make_pair(A[i], i));
        }

        return water;
    }
};


//AZL

## 双数组

C++ Code:

```c++
int trap(vector<int>& heights)
{
	if(heights == null)
		return 0;
    int ans = 0;
    int size = heights.size();
    vector<int> left_max(size), right_max(size);
    left_max[0] = heights[0];
    for (int i = 1; i < size; i++) {
        left_max[i] = max(heights[i], left_max[i - 1]);
    }
    right_max[size - 1] = heights[size - 1];
    for (int i = size - 2; i >= 0; i--) {
        right_max[i] = max(heights[i], right_max[i + 1]);
    }
    for (int i = 1; i < size - 1; i++) {
        ans += min(left_max[i], right_max[i]) - heights[i];
    }
    return ans;
}


## 双指针

上面代码比较好理解，但是需要额外的 N 的空间。从上面解法可以看出，我们实际上只关心左右两侧较小的那一个，并不需要两者都计算出来。具体来说：

- 如果 l[i + 1] < r[i] 那么 最终积水的高度由 i 的左侧最大值决定。
- 如果 l[i + 1] >= r[i] 那么 最终积水的高度由 i 的右侧最大值决定。

因此我们不必维护完整的两个数组，而是可以只进行一次遍历，同时维护左侧最大值和右侧最大值，使用常数变量完成即可。这是一个典型的双指针问题，


//AZL
C++ Code:

```c++

class Solution {
public:
    int trap(vector<int>& heights)
{
    int left = 0, right = heights.size() - 1;
    int ans = 0;
    int left_max = 0, right_max = 0;
    while (left < right) {
        if (heights[left] < heights[right]) {
            heights[left] >= left_max ? (left_max = heights[left]) : ans += (left_max - heights[left]);
            ++left;
        }
        else {
            heights[right] >= right_max ? (right_max = heights[right]) : ans += (right_max - heights[right]);
            --right;
        }
    }
    return ans;
}

};
```