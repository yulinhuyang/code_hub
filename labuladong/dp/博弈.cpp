class Solution {
public:
    unordered_map<int, int> memo;

    int dfs(vector<int> &piles, int index) {
        // 从两边向中间获取
        // index 值为 1/2 piles.size() 时可以停止算法
        if (index == piles.size() / 2)
            return 0;

        // 减少计算，快速返回已有结果
        if (memo.count(index))
            return memo[index];

        // 防止第一次取最右时越界
        int n = piles.size() - 1;

        // 先手选择最左边或最右边后的分数
        int l = piles[index] + dfs(piles, index + 1);
        int r = piles[n - index] + dfs(piles, index + 1);

        // 返回先手左或右边的最高分
        return memo[index] = max(l, r);
    }

   bool stoneGame(vector<int>& piles) {
        // 最佳发挥时：
        // 先手得分 * 2 > 总大小 则先手者胜利
        return dfs(piles, 0) * 2 > accumulate(begin(piles), end(piles), 0);
    }
};
