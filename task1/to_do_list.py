import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Enter task👉: ")
    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added!✅")

def view_tasks():
    if not tasks:
        print("No tasks yet.❌")
        return

    for i, task in enumerate(tasks):
        status = "Done👍" if task["done"] else "Pending⚠️"
        print(f"{i+1}. {task['title']} - {status}")

def mark_done():
    view_tasks()
    if not tasks:
        return
    num = int(input("Enter task number to mark done: "))
    tasks[num-1]["done"] = True
    save_tasks()
    print("Task marked as done!⭕")

def delete_task():
    view_tasks()
    if not tasks:
        return

    num = int(input("Enter task number to delete: "))

    if num < 1 or num > len(tasks):
        print("Invalid task number")
        return

    tasks.pop(num-1)
    save_tasks()
    print("Task deleted⭕!")


load_tasks()

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose option👉: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice !")
