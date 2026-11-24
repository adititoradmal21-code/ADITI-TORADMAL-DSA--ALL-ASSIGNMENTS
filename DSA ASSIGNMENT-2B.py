
queue = []
MAX_SIZE = 100

while True:
    print("\n--- FOOD DELIVERY ORDER QUEUE ---")
    print("1. Place Order (Enqueue)")
    print("2. Prepare Order (Dequeue)")
    print("3. View Next Order")
    print("4. Display Order Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if len(queue) == MAX_SIZE:
            print("Queue Overflow! Cannot accept new orders.")

        else:
            order_id = input("Enter Order ID: ")

            duplicate = False

            for order in queue:
                if order[0] == order_id:
                    duplicate = True
                    break

            if duplicate:
                print("Duplicate Order ID is not allowed.")

            else:
                status = input("Is the order confirmed? (Yes/No): ")

                if status.lower() == "yes":
                    queue.append(order_id)
                    print("Order placed successfully.")

                else:
                    print("Only confirmed orders are accepted.")

    elif choice == 2:

        if len(queue) == 0:
            print("Queue Underflow! No orders available.")

        else:
            prepared = queue.pop(0)
            print("Order Prepared:", prepared)

    elif choice == 3:

        if len(queue) == 0:
            print("No pending orders.")

        else:
            print("Next Order to Prepare:", queue[0])

    elif choice == 4:

        if len(queue) == 0:
            print("Order Queue is Empty.")

        else:
            print("\nFood Delivery Order Queue:")
            for order in queue:
                print(order)

    elif choice == 5:
        print("Exiting Food Delivery Order Queue.")
        break

    else:
        print("Invalid Choice! Try Again.")

