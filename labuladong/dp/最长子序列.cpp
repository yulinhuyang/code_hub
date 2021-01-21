class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        /* len 为牌的数量 */
        int len = nums.size();
        vector<int> top(len, 0);
        /* 牌堆数初始化为0 */
        int piles = 0;
        for (int i = 0; i < len; i++) {
            /* nums[i] 为要处理的扑克牌 */
            int poker = nums[i];

            /***** 搜索左侧边界的二分查找 *****/
            int left = 0, right = piles;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (top[mid] > poker) {
                    right = mid;
                } else if (top[mid] < poker) {
                    left = mid + 1;
                } else if (top[mid] == poker) {
                    right = mid;
                }
            }
            /*********************************/

            /* 没找到合适的牌堆，新建一堆 */
            if (left == piles)
                piles++;
            /* 把这张牌放到牌堆顶 */
            top[left] = poker;
        }
        /* 牌堆数就是 LIS 长度 */
        return piles;
    }
};
