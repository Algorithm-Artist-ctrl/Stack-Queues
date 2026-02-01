def is_balanced(s):
    stack = []
    match = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
    return len(stack) == 0
s = "{}()[]"
print(is_balanced(s))   
s = "{[()]}"
print(is_balanced(s))   
s = "{[(])}"
print(is_balanced(s))  
