## 题目描述

```
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

```

## 前置知识

- 回溯法


//AZL
Python3 Code:

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯法，层层递减，得到符合条件的路径就加入结果集中，超出则剪枝；
        主要是要注意一些细节，避免重复等；
        """
        size = len(candidates)
        if size <= 0:
            return []

        # 先排序，便于后面剪枝
        candidates.sort()

        path = []
        res = []
        self._find_path(target, path, res, candidates, 0, size)

        return res

    def _find_path(self, target, path, res, candidates, begin, size):
        """沿着路径往下走"""
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                # 如果剩余值为负数，说明超过了，剪枝
                if left_num < 0:
                    break
                # 否则把当前值加入路径
                path.append(candidates[i])
                # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除，
                # 因为根据他们得出的解一定在之前就找到过了
                self._find_path(left_num, path, res, candidates, i, size)
                # 记得把当前值移出路径，才能进入下一个值的路径
                path.pop()
