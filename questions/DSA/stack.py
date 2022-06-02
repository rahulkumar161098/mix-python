def create_stack():
    stack=[]
    return stack
    
def check_empty(stack):
    return len(stack)== 0


def push(stack, item):
    stack.append(item)
    print('pushed item '+ item)
    
def pop(stack):
    if create_stack()==0:
        print("stack is empty")
    return stack.pop


stack=create_stack()
push(stack, str(3))
push(stack, str(35))
push(stack, str(5))
print('stack', stack)