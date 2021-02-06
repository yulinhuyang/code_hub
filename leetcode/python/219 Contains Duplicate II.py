## 题目描述


```
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

 

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

```

## 前置知识

- hashmap

# Method 1: using set

def containsNearbyDuplicate(self, nums, k):
    if len(nums) <= k + 1: return len(nums) != len(set(nums))
    if k == 0: return False
    s = set(nums[:k])
    for i in range(k, len(nums)):
        if nums[i] in s: return True
        else:
            s.remove(nums[i - k])
            s.add(nums[i])
    return False

# Method 2: using dictionary
def containsNearbyDuplicate(self, nums, k):
    d = {}
    for i, n in enumerate(nums):
        if n in d and i - d[v] <= k:
            return True
        d[n] = i
    return False


#azl

Python Code:

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, num in enumerate(nums):
            if num in d and index - d[num] <= k:
                return True
            d[num] = index
        return False
```