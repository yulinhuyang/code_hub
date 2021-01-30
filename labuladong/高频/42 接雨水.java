Yifan Zhang 提供 java 代码

//双指针解法：时间复杂度 O(N)，空间复杂度 O(1)

对cpp版本的解法有非常微小的优化。
因为我们每次循环只会选 left 或者 right 处的柱子来计算，因此我们并不需要在每次循环中同时更新maxLeft和maxRight。
我们可以先比较 maxLeft 和 maxRight，决定这次选择计算的柱子是 height[left] 或者 height[right] 后再更新对应的 maxLeft 或 maxRight。
当然这并不会在时间上带来什么优化，只是提供一种思路。

class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int left = 0, right = height.length - 1;
        int maxLeft = height[left], maxRight = height[right];
        int res = 0;
        
        while (left < right) {
            // 比较 maxLeft 和 maxRight，决定这次计算 left 还是 right 处的柱子
            if (maxLeft < maxRight) {
                left++;
                maxLeft = Math.max(maxLeft, height[left]);  // update maxLeft
                res += maxLeft - height[left];
            } else {
                right--;
                maxRight = Math.max(maxRight, height[right]);   // update maxRight
                res += maxRight - height[right];
            }
        }
        
        return res;
    }
}


附上暴力解法以及备忘录解法的 java 代码

//暴力解法：时间复杂度 O(N^2)，空间复杂度 O(1)

class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int n = height.length;
        int res = 0;
        // 跳过最左边和最右边的柱子，从第二个柱子开始
        for (int i = 1; i < n - 1; i++) {
            int maxLeft = 0, maxRight = 0;
            // 找右边最高的柱子
            for (int j = i; j < n; j++) {
                maxRight = Math.max(maxRight, height[j]);
            }
            // 找左边最高的柱子
            for (int j = i; j >= 0; j--) {
                maxLeft = Math.max(maxLeft, height[j]);
            }
            // 如果自己就是最高的话，
            // maxLeft == maxRight == height[i]
            res += Math.min(maxLeft, maxRight) - height[i];
        }
        return res;
    }
}


//备忘录解法：时间复杂度 O(N)，空间复杂度 O(N)

class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int n = height.length;
        int res = 0;
        // 数组充当备忘录
        int[] maxLeft = new int[n];
        int[] maxRight = new int[n];
        // 初始化 base case 
        maxLeft[0] = height[0];
        maxRight[n - 1] = height[n - 1];
        
        // 从左向右计算 maxLeft
        for (int i = 1; i < n; i++) {
            maxLeft[i] = Math.max(maxLeft[i - 1], height[i]);
        }
        // 从右向左计算 maxRight
        for (int i = n - 2; i >= 0; i--) {
            maxRight[i] = Math.max(maxRight[i + 1], height[i]);
        }
        // 计算答案
        for (int i = 1; i < n; i++) {
            res += Math.min(maxLeft[i], maxRight[i]) - height[i];
        }
        return res;
    }
}
