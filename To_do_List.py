#To-Do List application in Python using a command-line interface (CLI)
tasks = []

def create_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date: ")
    priority = input("Enter priority (high/medium/low): ")
    
    task = {
        "name": task_name,
        "due_date": due_date,
        "priority": priority
    }
    
    tasks.append(task)
    print("Task added successfully!")

def display_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} (Due: {task['due_date']}, Priority: {task['priority']})")

def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            create_task()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()