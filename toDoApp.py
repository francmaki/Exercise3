# toDoApp.py

tasksarray = []
def addtask(task):
    # Add a task if it's not empty
    if task.strip() == "":
        print("Task cannot be empty!")
    else:
        tasksarray.append(task)
        print("Succesfully added task!")
        
        
def showTasks():
    # Show all tasks through for loop
    if len(tasksarray) == 0:
        print("No tasks yet!")
    else:
        print("These are your remaining tasks: ")
        for i in range(len(tasksarray)):
            print(str(i+1) + ". " + tasksarray[i].title())
            
            
def removetask(tasknumber):
     # Remove a task by number given through user input
    if tasknumber < 1 or tasknumber > len(tasksarray):
        print("Invalid task number!")
    else:
        tasksarray.pop(tasknumber - 1)
        print("Task removed!")
        
        
def main():
    # Main menu loop using while
    while True:
        print("TO DO APPPLICATION!")
        print("=====================================")
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        choice = input("Enter choice: ")
        print()
        
        if choice == "1":
            # Ask the user to input a new task
            task = input("Please enter the task: ")
            addtask(task)
            print("\n")
        elif choice == "2":
            showTasks()
        elif choice == "3":
            # Remove a task if tasks exist
            if len(tasksarray) == 0:
                print("No tasks to remove!\n")
                continue
            try:
                num = int(input("Enter task no to remove: "))
                removetask(num)
                print("\n")
            except ValueError:
                 # Handles non-integer input
                print("Invalid input! Enter a number.\n")
        elif choice == "4":
            break
        else:
             # Handle invalid menu option
            print("Wrong choice!!")

main()