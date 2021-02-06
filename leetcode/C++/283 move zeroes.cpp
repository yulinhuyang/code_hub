## 题目描述
```
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

```

## 前置知识

- [数组](https://github.com/azl397985856/leetcode/blob/master/thinkings/basic-data-structure.md)
- 双指针


//azl

C++ Code：

> 解题思想与上面 JavaScript 一致，做了少许代码优化（非性能优化，因为时间复杂度都是 O(n)）：
> 增加一个游标来记录下一个待处理的元素的位置，这样只需要写一次循环即可。

```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int>::size_type nonZero = 0;
        vector<int>::size_type next = 0;
        while (next < nums.size()) {
            if (nums[next] != 0) {
                // 使用 std::swap() 会带来 8ms 的性能损失
                // swap(nums[next], nums[nonZero]);
                auto tmp = nums[next];
                nums[next] = nums[nonZero];
                nums[nonZero] = tmp;
                ++nonZero;
            }
            ++next;
        }
    }
};
```
