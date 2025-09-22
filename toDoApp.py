# toDoApp.py

tasks = []
def addtask(task):
    if task.strip() == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        print("Task added!")
def showTasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("Tasks: ")
        for i in range(len(tasks)):
            print(str(i+1) + ". " + tasks[i].title())
def removetask(tasknumber):
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid task number!")
    else:
        tasks.pop(tasknumber - 1)
        print("Task removed!")
def main():
    while True:
        print()
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("Enter choice: ")
        print()
        if ch == "1":
            t = input("Enter task: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            if len(tasks) == 0:
                print("No tasks to remove!")
                continue
            try:
                n = int(input("Enter task no to remove: "))
                removetask(n)
            except ValueError:
                print("Invalid input! Enter a number.")
        elif ch == "4":
            break
        else:
            print("Wrong choice!!")

main()