#To-Do List

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def update_task():
    task_num = int(input("Enter the task number to update: ")) - 1
    if task_num < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num] = new_task
        print(f"Task '{new_task}' updated!")
    else:
        print("Invalid task number!")

def delete_task():
    task_num = int(input("Enter the task number to delete: ")) - 1
    if task_num < len(tasks):
        del tasks[task_num]
        print("Task deleted!")
    else:
        print("Invalid task number!")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")