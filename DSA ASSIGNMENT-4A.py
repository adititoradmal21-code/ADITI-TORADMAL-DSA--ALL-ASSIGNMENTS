
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive Postorder Traversal
def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# Create Expression Tree
root = Node('+')

root.left = Node('*')
root.right = Node('-')

root.left.left = Node('A')
root.left.right = Node('B')

root.right.left = Node('C')
root.right.right = Node('D')


# Display Postfix Expression
print("Postfix Expression:")
postorder(root)
