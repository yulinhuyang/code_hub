// LeetCode, Length of Last Word
// 偷懒，用 STL
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    int lengthOfLastWord(const string& s) {
        auto first = find_if(s.rbegin(), s.rend(), ::isalpha);
        auto last = find_if_not(first, s.rend(), ::isalpha);
        return distance(first, last);
    }
};



// LeetCode, Length of Last Word
// 顺序扫描，记录每个 word 的长度
// 时间复杂度O(n)，空间复杂度O(1)
class Solution {
public:
    int lengthOfLastWord(const string& s) {
        return lengthOfLastWord(s.c_str());
    }
private:
    int lengthOfLastWord(const char *s) {
        int len = 0;
        while (*s) {
            if (*s++ != ' ')
                ++len;
            else if (*s && *s != ' ')
                len = 0;
        }
        return len;
    }
};

