from task import Task

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                task_name, task_status = line.strip().split(',')
                task = Task(task_name, task_status == 'True')
                self.tasks.append(task)

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.name},{task.completed}\n")

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.complete()
                break

    def show_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            status = "Done" if task.completed else "Not Done"
            print(f"- {task.name} ({status})")

if __name__ == "__main__":
    manager = ToDoListManager()
    manager.load_tasks("data/tasks.txt")

    while True:
        print("\nToDo List Manager")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Save and Exit")

        choice = input("Select an option: ")

        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            task_name = input("Enter task name: ")
            manager.add_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name to mark as complete: ")
            manager.complete_task(task_name)
        elif choice == "4":
            manager.save_tasks("data/tasks.txt")
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
