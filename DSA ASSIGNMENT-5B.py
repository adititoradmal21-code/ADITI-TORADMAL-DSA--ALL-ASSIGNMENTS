
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert node into BST
def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    else:
        root.right = insert(root.right, data)

    return root


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

    print("Postorder Traversal:")

    while len(stack2) > 0:

        temp = stack2.pop()
        print(temp.data, end=" ")


# Main Program
root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

postorder(root)
