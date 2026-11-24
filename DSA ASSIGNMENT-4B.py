
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Non-Recursive Postorder using Two Stacks
def postorder(root):

    if root is None:
        return

    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1) > 0:

        temp = stack1.pop()
        stack2.append(temp)

        if temp.left is not None:
            stack1.append(temp.left)

        if temp.right is not None:
            stack1.append(temp.right)

    print("Postfix Expression:")

    while len(stack2) > 0:
        temp = stack2.pop()
        print(temp.data, end=" ")


# Create Expression Tree
root = Node('+')

root.left = Node('*')
root.right = Node('-')

root.left.left = Node('A')
root.left.right = Node('B')

root.right.left = Node('C')
root.right.right = Node('D')


# Display Postfix Expression
postorder(root)
