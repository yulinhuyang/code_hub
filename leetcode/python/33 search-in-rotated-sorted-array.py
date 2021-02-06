题目描述
``` 给你一个升序排列的整数数组 nums ，和一个整数 target 。
假设按照升序排序的数组在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
  示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0 输出：4 示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3 输出：-1 示例 3：
输入：nums = [1], target = 0 输出：-1  
提示：
1 <= nums.length <= 5000 -10^4 <= nums[i] <= 10^4 nums 中的每个值都 独一无二 nums 肯定会在某个点上旋转 -10^4 <= target <= 10^4
```

//AZL

Python3 Code:
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """用二分法，先判断左右两边哪一边是有序的，再判断是否在有序的列表之内"""
        if len(nums) <= 0:
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            
            # 如果中间的值大于最左边的值，说明左边有序
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    # 这里 +1，因为上面是 <= 符号
                    left = mid + 1
            # 否则右边有序
            else:
                # 注意：这里必须是 mid+1，因为根据我们的比较方式，mid属于左边的序列
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
                    
        return left if nums[left] == target else -1
 
