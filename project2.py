import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['task']} [{status}]")


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        tasks[task_num]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        task = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"Deleted task: {task['task']}")
    except (IndexError, ValueError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
