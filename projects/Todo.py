def list_all_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nAll Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{index}. {task['title']} - {task['description']} (Priority: {task['priority']}, Status: {status})")

def add_task(tasks):
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    priority = input("Enter the priority of the task (Low/Medium/High): ")
    task = {
        'title': title,
        'description': description,
        'priority': priority,
        'completed': False  
    }
    tasks.append(task)
    print("Task added successfully.")

def update_task(tasks):
    list_all_tasks(tasks)
    task_number = int(input("Enter the task number you want to update: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        task['title'] = input(f"Enter new title (current: {task['title']}): ") or task['title']
        task['description'] = input(f"Enter new description (current: {task['description']}): ") or task['description']
        task['priority'] = input(f"Enter new priority (current: {task['priority']}): ") or task['priority']
        status = input(f"Enter new status (current: {'Completed' if task['completed'] else 'Pending'}): ")
        task['completed'] = True if status.lower() == "completed" else False
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    list_all_tasks(tasks)
    task_number = int(input("Enter the task number you want to delete: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nWELCOME TO THE TASK MANAGEMENT APP")
        print("1. View all tasks.")
        print("2. Add new task.")
        print("3. Update a task.")
        print("4. Delete a task.")
        print("5. Exit the app.")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_tasks(tasks)
            case '2':
                add_task(tasks)
            case '3':
                update_task(tasks)
            case '4':
                delete_task(tasks)
            case '5':
                print("Thank you for using the Task Management App. Goodbye!")
                break
            case _:
                print("Wrong entry. Please enter a valid option.")

if __name__ == "__main__":
    main()