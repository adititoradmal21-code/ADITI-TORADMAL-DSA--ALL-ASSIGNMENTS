
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


# Non-Recursive Preorder Traversal
def preorder(root):

    if root is None:
        return

    stack = []
    stack.append(root)

    print("Preorder Traversal:")

    while len(stack) > 0:

        temp = stack.pop()
        print(temp.data, end=" ")

        if temp.right is not None:
            stack.append(temp.right)

        if temp.left is not None:
            stack.append(temp.left)


# Main Program
root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

preorder(root)

