
queue = []
MAX_SIZE = 30

while True:
    print("\n--- PRINTER JOB QUEUE ---")
    print("1. Add Print Job (Enqueue)")
    print("2. Print Job (Dequeue)")
    print("3. View Next Job")
    print("4. Display Print Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if len(queue) == MAX_SIZE:
            print("Queue is Full! Cannot add new job.")

        else:
            job_id = input("Enter Job ID: ")

            duplicate = False

            for job in queue:
                if job[0] == job_id:
                    duplicate = True
                    break

            if duplicate:
                print("Duplicate Job ID is not allowed.")

            else:
                file_type = input("Enter File Type (PDF/DOCX): ")

                if file_type.lower() == "pdf" or file_type.lower() == "docx":
                    queue.append((job_id, file_type.upper()))
                    print("Print Job Added Successfully.")

                else:
                    print("Invalid File Type! Only PDF and DOCX allowed.")

    elif choice == 2:

        if len(queue) == 0:
            print("Queue is Empty! No jobs to print.")

        else:
            printed = queue.pop(0)
            print("Printing Job:", printed)

    elif choice == 3:

        if len(queue) == 0:
            print("No Pending Print Jobs.")

        else:
            print("Next Job to Print:", queue[0])

    elif choice == 4:

        if len(queue) == 0:
            print("Print Queue is Empty.")

        else:
            print("\nPrint Jobs in Queue:")
            for job in queue:
                print(job)

    elif choice == 5:
        print("Exiting Printer Job Queue.")
        break

    else:
        print("Invalid Choice! Try Again.")
