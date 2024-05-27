is_on = True
task_list = []
def add_task(tasklist):
    
    task = input("Enter your task: ")
    tasklist.append(task)
    
def view_task(tasklist):
    if len(tasklist) == 0:
            print("No tasks available.")
    else:
        print("TERE TASKS: ")
        for index, task in enumerate(tasklist, start=1):
            print(f"{index}. {task}")
def mark_as_done(tasklist):
    if len(tasklist) == 0:
        print("No tasks available.")
    else:
        view_task(tasklist)
        choice_mad = input("Select the task to be marked as done: ")
        if choice_mad.isdigit():
            choice_mad = int(choice_mad)
            if choice_mad > len(tasklist):
                print("Please pick a valid number")
            else:
                tasklist[choice_mad - 1] += " (DONE)"
                print("Marked as done.")
        else:
            print("Invalid input.")
def delete_task(tasklist):
    
    if len(tasklist) == 0:
        print("No tasks available")
    else:
        view_task(tasklist)
        choice_del = input("Please select a task to delete: ")
        
        if choice_del.isdigit():
            choice_del = int(choice_del)
            if 1 <= choice_del <= len(tasklist):
                del tasklist[choice_del - 1]
                print("Task deleted.")
            else:
                print("Please pick a valid number.")
        else:
            print("Please pick a valid number")

        
    
    
    
while is_on:
    print("Sambhav's To-Do List")
    print("1. Add a task")
    print("2. View your tasks")
    print("3. Mark as done")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice.isdigit():
        choice = int(choice)
    else:
        print("OH BHAI BHAI BHAI!! 1 se 5 ke bich ka number daal!")
    
    if choice == 1:
        add_task(task_list)
        print("TASK DALGAYA")
    elif choice == 2:
        view_task(task_list)
    elif choice == 3:
        mark_as_done(task_list)
    elif choice == 4:
        delete_task(task_list)
    elif choice == 5:
        is_on = False
    
        
    
    