
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert product at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    # Delete a product
    def delete(self, key):

        if self.head is None:
            print("List is Empty.")
            return

        if self.head.data == key:
            self.head = self.head.next
            print("Product", key, "deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:

            if temp.next.data == key:
                temp.next = temp.next.next
                print("Product", key, "deleted successfully.")
                return

            temp = temp.next

        print("Product not found.")

    # Display product list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
cart = LinkedList()

# Create current product list
cart.insert(501)
cart.insert(502)
cart.insert(503)
cart.insert(504)

# Display current list
print("Current Product List:")
cart.display()

# Insert Product 505
cart.insert(505)

# Delete Product 503
cart.delete(503)

# Display final list
print("Final Product List:")
cart.display()
