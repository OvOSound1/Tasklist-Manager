# Names: Francisco Fausto, Tiffany Nguyen, Nick Breeding 
# Assignment: Lab 12, Group 9
# Course: CECS 277 Sec 04
# Date: April 30th, 2024
# Desc: You can create a Python program that manages a task list for the user. The program reads tasks from a file ('tasklist.txt') at startup and allows the user to view the current task, list all tasks, mark tasks as complete, search by date, and add new tasks, saving the updated list back to the file when the program quits.

from tasklist import Tasklist

def main_menu():
    """
    Displays the main menu and prompts the user for a choice.

    Returns:
        str: The user's choice.
    """
    print("-Tasklist-")
    print("\nTasks to complete: ", len(tasklist))
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    choice = input("Enter choice: ")
    return choice

def get_date():
    """
    Prompts the user to input a date.

    Returns:
        str: The user's input date.
    """
    month = input("Enter month: ")
    day = input("Enter day: ")
    year = input("Enter year: ")
    return f"{month}/{day}/{year}"

def get_time():
    """
    Prompts the user to input a time.

    Returns:
        str: The user's input time.
    """
    hour = input("Enter hour: ")
    minute = input("Enter minute: ")
    return f"{hour}:{minute}"

if __name__ == "__main__":
    tasklist = Tasklist()
    while True:
        choice = main_menu()
        if choice == '1':
            print("\nCurrent task is:")
            print(tasklist.get_current_task())
        elif choice == '2':
            print("\nTasks:\n")
            for task in tasklist:
                print(task)
        elif choice == '3':
            print("\nMarking current task as complete:")
            tasklist.mark_complete()
            print("New current task is:")
            print(tasklist.get_current_task())
        elif choice == '4':
            desc = input("Enter a task: ")
            print("Enter due date:")
            date = get_date()
            time = get_time()
            tasklist.add_task(desc, date, time)
        elif choice == '5':
            print("Enter date to search: ")
            date = get_date()
            print("\nTasks due on", date, ":\n")
            for task in tasklist:
                if task.date == date:
                    print(task)
        elif choice == '6':
            print("Saving List...")
            tasklist.save_file()
            break
