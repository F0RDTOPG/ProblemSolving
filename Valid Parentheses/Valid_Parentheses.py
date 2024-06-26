def Valid_Parentheses(string):
    stack = []
    ClosetoOpen = {'(': ')', '[': ']', '{': '}'}
    for c in string:
        if c in ClosetoOpen:
            if stack and stack[-1] == ClosetoOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False