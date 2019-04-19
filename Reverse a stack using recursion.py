def reverse(stack):
    l = len(stack)
    # print(stack)
    if l>0:
        x = stack.pop()
        reverse(stack)
        insertAtBottom(stack, x)
        # print(stack)
    # print(stack)


def insertAtBottom(stack, x):
    if len(stack) == 0:
        stack.append(x)
        return
    a = stack.pop()
    insertAtBottom(stack, x)
    stack.append(a)


def prints(stack):
    l = len(stack)
    for i in range(l - 1, -1, -1):
        print(stack[i], end=" ")


if __name__ == "__main__":
    stack = []
    stack.append(4)
    stack.append(3)
    stack.append(2)
    stack.append(1)
    print("Original Stack")
    prints(stack)
    reverse(stack)
    print("\nReversed Stack")
    prints(stack)
