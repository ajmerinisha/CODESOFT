import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def view_tasks(tasks):
    if not tasks:
        print("📝 No tasks available.")
        return

    print("\nYour To-Do List:")
    print("=" * 50)
    print("{:<5} {:<30} {:<10}".format("No.", "Task", "Status"))
    print("=" * 50)
    for idx, task in enumerate(tasks, start=1):
        status = "✅ Done" if task['completed'] else "❌ Pending"
        print("{:<5} {:<30} {:<10}".format(idx, task['title'], status))
    print("=" * 50)


def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("✅ Task added successfully!")
    else:
        print("❌ Task cannot be empty.")


def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("✅ Task marked as complete.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"🗑️ Deleted task: {deleted['title']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- 📋 To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("✅ Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
