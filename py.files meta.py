class Task  
{
  name: string;
  description: string;
  dueDate: Date;
  priority: string;

  constructor(name: string, description: string, dueDate: string, priority: string) {
    this.name = name;
    this.description = description;
    this.dueDate = new Date(dueDate);
    this.priority = priority;
  }

  toString(): string {
    return `${this.name}: ${this.description} (Due: ${this.dueDate.toDateString()}, Priority: ${this.priority})`;
  }
}class TaskScheduler {
  tasks: Task[];

  constructor() {
    this.tasks = [];
  }

  addTask(task: Task): void {
    this.tasks.push(task);
  }
  
  viewTasks(): void {
    for (const task of this.tasks) {
      console.log(task.toString());
    }
  }

  scheduleTasks(): void {
    this.tasks.sort((a, b) => {
      if (a.priority === b.priority) {
        return a.dueDate.getTime() - b.dueDate.getTime();
      }
      return this.getPriorityValue(b.priority) - this.getPriorityValue(a.priority);
    });
  }

  private getPriorityValue(priority: string): number {
    switch (priority.toLowerCase()) {
      case 'high':
        return 3;
      case 'medium':
        return 2;
      case 'low':
        return 1;
      default:
        return 0;
    }
  }
}function main(): void {
  const scheduler = new TaskScheduler();
  while (true) {
    console.log("1. Add Task");
    console.log("2. View Tasks");
    console.log("3. Schedule Tasks");
    console.log("4. Quit");
    const choice = prompt("Enter your choice: ");
    if (choice === "1") {
      const name = prompt("Enter task name: ");
      const description = prompt("Enter task description: ");
      const dueDate = prompt("Enter task due date (YYYY-MM-DD): ");
      const priority = prompt("Enter task priority (High/Medium/Low): ");
      const task = new Task(name, description, dueDate, priority);
      scheduler.addTask(task);
    } else if (choice === "2") {
      scheduler.viewTasks();
    } else if (choice === "3") {
      scheduler.scheduleTasks();
      scheduler.viewTasks();
    } else if (choice === "4") {
      break;
    } else {
      console.log("Invalid choice. Please try again.");
    }
  }
}

main();

