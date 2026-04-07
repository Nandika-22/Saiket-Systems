class task:
    def __init__(self,description):
        self.description=description
        self.completed=False
    def mark_completed(self):
        self.competed=True
class todolist:
    def __init__(self):
        self.tasks=[]
    def add_task(self,description):
        self.tasks.append(task(description))
        print("Task added successfully!")
    def view_tasks(self):
        if not self.tasks:
            print("No Tasks Available")
            return
        print("\nYour tasks:")
        for i,task in enumerate(self.tasks,start=1):
            status="completed" if task.completed else "Pending"
            print(f"{1}.{task.description}-{status}")
    def complete_task(self,task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number-1].mark_completed()
            print("tasks marked as completed!")
        else:
            print("Invalid task number.")
def main():
    todo=todolist()
    while True:
        print("\n----- TO-DO-LIST -----")
        print("1.Add Task")
        print("2.View task")
        print("Mark as Completed")
        print("Exit")
        choice=input("enter your choice(1-4):")
        if choice=="1":
            desc=input("enter task description:")
            todo.add_task(desc)
        elif choice=="2":
            todo.view_tasks()
        elif choice=="3":
            todo.view_tasks()
            num=int(input("enter task number to mark completed:"))
            todo.complete_task(num)
        elif choice=="4":
            print("Exiting to-do=apllication!")
            break
        else:
            print("invalid Choice.please try again!")
if __name__ == "__main__":
    main()
            






