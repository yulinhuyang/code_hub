//基本思想：每次遇到左括号时都将相对应的右括号'）'，']'或'}'推入堆栈
//如果在字符串中出现右括号，则需要检查堆栈是否为空，以及顶部元素是否与该右括号相同。如果不是，则该字符串无效。
//最后，我们还需要检查堆栈是否为空
public boolean isValid(String s) {
  Deque<Character> stack = new ArrayDeque<>();
  for(char c : s.toCharArray()){
    //是左括号就将相对应的右括号入栈
    if(c=='(') {
      stack.offerLast(')');
    }else if(c=='{'){
      stack.offerLast('}');
    }else if(c=='['){
      stack.offerLast(']');   
    }else if(stack.isEmpty() || stack.pollLast()!=c){//出现右括号，检查堆栈是否为空，以及顶部元素是否与该右括号相同
      return false;
    }
  }
  return stack.isEmpty();
}
