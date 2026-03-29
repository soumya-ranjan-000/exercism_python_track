def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in "({[":
            stack.append(char)
        elif char in ")]}":
            if len(stack) != 0:
                if char == ")":
                    if stack.pop() != '(':
                        return False
                if char == "]":
                    if stack.pop() != '[':
                        return False
                if char == "}":
                    if stack.pop() != '{':
                        return False
            else:
                return False
    return len(stack) == 0
