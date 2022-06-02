
def is_Valid(s):
    d={'(':')', '{':'}', '[':']'}
    stack=[]
    for i in s:
        if i in s:
            stack.append(i)
            # return stack
        elif(len(stack)>0 and i == stack[-1]):
            stack.pop()
            # return stack
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

print(is_Valid("(())"))