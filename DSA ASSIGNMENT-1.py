
stack = []
MAX_SIZE = 20

while True:
    print("\n--- CAFETERIA PLATE STACK ---")
    print("1. Add Plate (Push)")
    print("2. Remove Plate (Pop)")
    print("3. View Top Plate (Peek)")
    print("4. Display Plate Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(stack) == MAX_SIZE:
            print("Stack Overflow! Stack is Full.")

        else:
            plate_id = input("Enter Plate ID: ")

            duplicate = False

            for plate in stack:
                if plate[0] == plate_id:
                    duplicate = True
                    break

            if duplicate:
                print("Duplicate Plate ID is not allowed.")

            else:
                material = input("Enter Plate Material (Steel/Ceramic): ")

                if material.lower() == "steel" or material.lower() == "ceramic":
                    stack.append((plate_id, material))
                    print("Plate added successfully.")

                else:
                    print("Invalid Material! Only Steel and Ceramic allowed.")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow! No plates available.")

        else:
            removed = stack.pop()
            print("Removed Plate:", removed)

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is Empty.")

        else:
            print("Top Plate:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("Stack is Empty.")

        else:
            print("\nPlates in Stack (Top to Bottom):")
            for plate in reversed(stack):
                print(plate)

    elif choice == 5:
        print("Exiting Cafeteria Plate Stack.")
        break

    else:
        print("Invalid Choice! Please try again.")
