// LeetCode, Search for a Range
// 偷懒的做法，使用STL
// 时间复杂度O(logn)，空间复杂度O(1)
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        const int l = distance(nums.begin(), lower_bound(nums.begin(), nums.end(), target));
        const int u = distance(nums.begin(), prev(upper_bound(nums.begin(), nums.end(), target)));
        if (nums[l] != target) // not found
            return vector<int> { -1, -1 };
        else
            return vector<int> { l, u };
    }
};




// LeetCode, Search for a Range
// 重新实现 lower_bound 和 upper_bound
// 时间复杂度O(logn)，空间复杂度O(1)
class Solution {
public:
    vector<int> searchRange (vector<int>& nums, int target) {
        auto lower = lower_bound(nums.begin(), nums.end(), target);
        auto uppper = upper_bound(lower, nums.end(), target);

        if (lower == nums.end() || *lower != target)
            return vector<int> { -1, -1 };
        else
            return vector<int> {distance(nums.begin(), lower), distance(nums.begin(), prev(uppper))};
    }

    template<typename ForwardIterator, typename T>
    ForwardIterator lower_bound (ForwardIterator first,
            ForwardIterator last, T value) {
        while (first != last) {
            auto mid = next(first, distance(first, last) / 2);

            if (value > *mid)   first = ++mid;
            else                last = mid;
        }

        return first;
    }

    template<typename ForwardIterator, typename T>
    ForwardIterator upper_bound (ForwardIterator first,
            ForwardIterator last, T value) {
        while (first != last) {
            auto mid = next(first, distance (first, last) / 2);

            if (value >= *mid)   first = ++mid;  // 与 lower_bound 仅此不同
            else                 last = mid;
        }

        return first;
    }
};

