
stack = []
MAX_SIZE = 25

while True:
    print("\n--- UNDO OPERATION IN TEXT EDITOR ---")
    print("1. Perform Action (Push)")
    print("2. Undo Action (Pop)")
    print("3. Last Action (Peek)")
    print("4. Display Action Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if len(stack) == MAX_SIZE:
            print("Stack Overflow! Maximum actions reached.")

        else:
            action = input("Enter Action (Insert/Delete/Replace): ")

            if action.lower() == "insert" or action.lower() == "delete" or action.lower() == "replace":

                if len(stack) > 0 and stack[-1].lower() == action.lower():
                    print("Consecutive duplicate action not allowed.")

                else:
                    stack.append(action.capitalize())
                    print("Action performed successfully.")

            else:
                print("Invalid Action! Action ignored.")

    elif choice == 2:

        if len(stack) == 0:
            print("Stack Underflow! No action to undo.")

        else:
            removed = stack.pop()
            print("Undo Action:", removed)

    elif choice == 3:

        if len(stack) == 0:
            print("No actions available.")

        else:
            print("Last Action:", stack[-1])

    elif choice == 4:

        if len(stack) == 0:
            print("Action Stack is Empty.")

        else:
            print("\nAction Stack (Top to Bottom):")
            for action in reversed(stack):
                print(action)

    elif choice == 5:
        print("Exiting Text Editor.")
        break

    else:
        print("Invalid Choice! Try Again.")
