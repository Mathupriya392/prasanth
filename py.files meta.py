import datetime

class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.name}: {self.description} (Due: {self.due_date}, Priority: {self.priority})"

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def schedule_tasks(self):
        self.tasks.sort(key=lambda x: x.due_date)
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

    def delete_task(self, task_number):
        try:
            task_choice = int(task_choice)
            if task_choice <= len(self.tasks):
                del self.tasks[task_choice - 1]
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid task number!")

    def resolve_dependencies(self):
        # Resolve task dependencies
        pass

def main():
    scheduler = TaskScheduler()
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Schedule Tasks")
        print("4. Delete Task")
        print("5. Resolve Dependencies")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            task = Task(name, description, due_date, priority)
            scheduler.add_task(task)
        elif choice == "2":
            scheduler.view_tasks()
        elif choice == "3":
            scheduler.schedule_tasks()
            scheduler.view_tasks()
        elif choice == "4":
            scheduler.view_tasks()
            task_number = input("Enter the task number to delete: ")
            scheduler.delete_task(task_number)
        elif choice == "5":
            scheduler.resolve_dependencies()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
