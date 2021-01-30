
#一种括号
bool isValid(string str) {
    // 待匹配的左括号数量
    int left = 0;
    for (char c : str) {
        if (c == '(')
            left++;
        else // 遇到右括号
            left--;

        if (left < 0)
            return false;
    }
    return left == 0;
}

#多种
bool isValid(string str) {
    stack<char> left;
    for (char c : str) {
        if (c == '(' || c == '{' || c == '[')
            left.push(c);
        else // 字符 c 是右括号
            if (!left.empty() && leftOf(c) == left.top())
                left.pop();
            else
                // 和最近的左括号不匹配
                return false;
    }
    // 是否所有的左括号都被匹配了
    return left.empty();
}

char leftOf(char c) {
    if (c == '}') return '{';
    if (c == ')') return '(';
    return '[';
}
