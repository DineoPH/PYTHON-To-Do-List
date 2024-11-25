tasks = []  # Initialize an empty task list

while True:
    # Display the menu
    print("\nTo-Do List Menu")
    print("1. Add Task\n2. View Tasks\n3. Mark Task Done\n4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":  # Add a task
        task_name = input("Enter the task: ")
        tasks.append({"task": task_name, "done": False})  # Add a new task
        print(f"Task '{task_name}' added!")

    elif choice == "2":  # View all tasks
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):  # Enumerate adds an index
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

    elif choice == "3":  # Mark a task as done
        try:
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <= len(tasks):  # Ensure the task number is valid
                tasks[task_num - 1]["done"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":  # Exit the program
        print("Exiting the To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
