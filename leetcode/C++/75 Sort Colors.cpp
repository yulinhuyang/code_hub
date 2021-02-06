
## 题目描述

```
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

```

// LeetCode, Sort Colors
// Counting Sort
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    void sortColors(vector<int>& A) {
        int counts[3] = { 0 }; // 记录每个颜色出现的次数

        for (int i = 0; i < A.size(); i++)
            counts[A[i]]++;

        for (int i = 0, index = 0; i < 3; i++)
            for (int j = 0; j < counts[i]; j++)
                A[index++] = i;

    }
};




// LeetCode, Sort Colors
// 双指针，时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    void sortColors(vector<int>& A) {
        // 一个是red的index，一个是blue的index，两边往中间走
        int red = 0, blue = A.size() - 1;

        for (int i = 0; i < blue + 1;) {
            if (A[i] == 0)
                swap(A[i++], A[red++]);
            else if (A[i] == 2)
                swap(A[i], A[blue--]);
            else
                i++;
        }
    }
};




// LeetCode, Sort Colors
// use partition()
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    void sortColors(vector<int>& nums) {
        partition(partition(nums.begin(), nums.end(), bind1st(equal_to<int>(), 0)),
                nums.end(), bind1st(equal_to<int>(), 1));
    }
};




// LeetCode, Sort Colors
// 重新实现 partition()
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    void sortColors(vector<int>& nums) {
        partition(partition(nums.begin(), nums.end(), bind1st(equal_to<int>(), 0)),
                 nums.end(), bind1st(equal_to<int>(), 1));
    }
private:
    template<typename ForwardIterator, typename UnaryPredicate>
    ForwardIterator partition(ForwardIterator first, ForwardIterator last,
            UnaryPredicate pred) {
        auto pos = first;

        for (; first != last; ++first)
            if (pred(*first))
                swap(*first, *pos++);

        return pos;
    }
};


//AZL
CPP Code:

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int r = 0, g = 0, b = 0;
        for (int n : nums) {
            if (n == 0) {
                nums[b++] = 2;
                nums[g++] = 1;
                nums[r++] = 0;
            } else if (n == 1) {
                nums[b++] = 2;
                nums[g++] = 1;
            } else nums[b++] = 2;
        }
    }
};