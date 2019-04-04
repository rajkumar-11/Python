class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isPairPresent(root, target):
    stack1 = []
    stack2 = []
    flag1 = True
    flag2 = True
    value1 = 0
    value2 = 0
    curr1 = root
    curr2 = root

    while (True):
        if (flag1):
            # print("here")
            while (curr1 is not None):
                stack1.append(curr1)
                curr1 = curr1.left
            if (len(stack1) == 0):
                flag1 = False
            else:
                curr1 = stack1.pop()
                value1 = curr1.data
                curr1 = curr1.right
                flag1 = False

        if (flag2):
            while (curr2 is not None):
                stack2.append(curr2)
                curr2 = curr2.right
            if (len(stack2) == 0):
                flag2 = False
            else:
                curr2 = stack2.pop()
                value2 = curr2.data
                curr2 = curr2.left
                flag2 = False
        print("value1= ", value1, "  value2= ", value2)

        if (value1 + value2 == target):
            print("Pair found ", value1, "+", value2, " = ", target)
            return

        if (value1 + value2 > target):
            flag2 = True
        elif (value1 + value2 < target):
            flag1 = True
        if (value1 >= value2):
            print("The pair is not present")
            return


if __name__ == "__main__":
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    isPairPresent(root, 20)
