
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a book at the end
    def insert(self, book_id):
        new_node = Node(book_id)

        if self.head is None:
            self.head = new_node

        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    # Display the linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
library = LinkedList()

# Create initial linked list
library.insert("B101")
library.insert("B102")
library.insert("B103")

# Insert new book IDs
library.insert("B104")
library.insert("B105")

# Display final linked list
print("Final Library Book IDs:")
library.display()
