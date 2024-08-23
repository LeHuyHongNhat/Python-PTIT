def count_remaining_elements(n, a):
    stack = []
    for num in a:
        # if stack is not empty and (first element in stack is + num) % 2 == 0
        # delete the element from the stack
        # ekse add the element to the stack
        if stack and (stack[-1] + num) % 2 == 0:
            stack.pop()
        else:
            stack.append(num)
    return len(stack)


n = int(input())
a = list(map(int, input().split()))

print(count_remaining_elements(n, a))
