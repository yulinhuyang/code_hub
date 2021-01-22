def isValid(self, s: str) -> bool:
    left = []
    leftOf = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for c in s:
        if c in '([{':
            left.append(c)
        elif left and leftOf[c]==left[-1]: # 右括号 + left不为空 + 和最近左括号能匹配
            left.pop()
        else: # 右括号 + （left为空 / 和堆顶括号不匹配）
            return False
        
    # left中所有左括号都被匹配则return True 反之False
    return not left
