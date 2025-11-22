# CSE Project: Simple Command-Line To-Do List Manager
'''
I have made this project for all the guys who wants a quick task list for them without
wasting much of their time as everyone in this world sometime struggles with the the thing 
they need to do throughout the day that is why i consider this as a real-world problem
 Objective of this project is to create a task list for the users and return them 
 a list of work or task they want or need to do throughout the day
'''

import os # Used to check if the data file exists


# The name of the file where the to-do list data will be saved
DATA_FILE = "todo_list.txt"
# The main data structure to hold our tasks (a list of strings)
todo_list = []

# functions used for file handling

def load_tasks():
    """
    Reads tasks from the DATA_FILE and loads them into the todo_list global variable.
    """
    global todo_list
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                # Read all lines, strip leading/trailing whitespace (like newline characters)
                todo_list = [line.strip() for line in file.readlines()]
            print(f"Tasks loaded from {DATA_FILE}.")
        except Exception as e:
            # Simple error handling for file reading issues
            print(f"Error loading tasks: {e}")
            todo_list = []
    else:
        print("No existing to-do file found. Starting with an empty list.")
        todo_list = []

def save_tasks():
    """
    Writes the current tasks from the todo_list back to the DATA_FILE.
    """
    try:
        with open(DATA_FILE, 'w') as file:
            # Write each task followed by a newline character
            for task in todo_list:
                file.write(task + '\n')
        print(f"\nTasks saved successfully to {DATA_FILE}.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# functons used for task management......

def add_task(task_description):
    """Adds a new task to the list."""
    if task_description.strip():
        todo_list.append(task_description.strip())
        print(f"Task added: '{task_description.strip()}'")
        save_tasks()
    else:
        print("Task description cannot be empty.")

def view_tasks():
    """Displays all tasks with their corresponding indices."""
    if not todo_list:
        print("\nYour to-do list is empty. Time to add some tasks!")
        return

    print("\n--- Current To-Do List ---")
    for index, task in enumerate(todo_list):
        # Index + 1 makes it user-friendly (starting at 1 instead of 0)
        print(f"{index + 1}. {task}")
    print("-" * 25)

def remove_task(task_index):
    """Removes a task by its 1-based index."""
    try:
        # Convert user input (1-based) to list index (0-based)
        index_to_remove = int(task_index) - 1

        if 0 <= index_to_remove < len(todo_list):
            removed_task = todo_list.pop(index_to_remove)
            print(f"Task removed: '{removed_task}'")
            save_tasks()
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

# loop for main application ....

def main_menu():
    """Main function to run the application interface."""

    # 1. Load tasks at the start
    load_tasks()

    print("\n" + "=" * 40)
    print("  To-Do List Manager (Persistent Storage)")
    print("=" * 40)

    while True:
        view_tasks()
        print("\nMenu:")
        print("  1. Add a new task")
        print("  2. Remove a task")
        print("  3. Exit and save")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            task = input("Enter the task description: ")
            add_task(task)

        elif choice == '2':
            if todo_list:
                task_num = input("Enter the number of the task to remove: ")
                remove_task(task_num)
            else:
                print("Cannot remove tasks from an empty list.")

        elif choice == '3':
            # save_tasks() is called within add_task and remove_task,
            # but it doesn't hurt to call it one last time before exit.
            print("Exiting To-Do List Manager. All changes saved.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()