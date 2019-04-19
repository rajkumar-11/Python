def sort(stack):
    if len(stack) > 0:
        x = stack.pop()
        sort(stack)
        sortUtil(stack, x)


def sortUtil(stack, x):
    if len(stack) is 0:
        stack.append(x)
        return
    a = stack.pop()
    if x > a:
        stack.append(a)
        stack.append(x)
        return
    sortUtil(stack, x)
    stack.append(a)


def prints(stack):
    l = len(stack)
    for i in range(l - 1, -1, -1):
        print(stack[i], end=" ")


if __name__ == "__main__":
    stack = []
    stack.append(26)
    stack.append(54)
    stack.append(34)
    stack.append(98)
    stack.append(120)
    stack.append(1111)
    stack.append(1)
    stack.append(2)
    print("Original Stack")
    prints(stack)
    sort(stack)
    print("\nSorted Stack")
    prints(stack)
