📝 Simple Command-Line To-Do List Manager (Python)

🌟 Project Overview

This project implements a straightforward and persistent Command-Line Interface (CLI) application designed to help users quickly manage their daily tasks and to-do lists.

The motivation behind this project is to provide a quick-access task manager that addresses the common problem of daily task organization. The core functionality is persistence: tasks are automatically saved to a local file, ensuring the list is preserved across sessions.

Objective

The primary objective is to offer users a reliable, persistent, and numbered list of tasks via a simple, intuitive command-line interface.

🛠️ Technology Used

Language: Python 3

Libraries: The standard os module for checking file existence.

Storage: Plain text file (todo_list.txt) for persistent data storage.

📦 How to Run the Application

Prerequisites

You must have Python 3 installed on your system.

Installation and Execution

Save the Code: Save the provided Python code into a file named, for example, todo_manager.py.

Open Terminal: Navigate to the directory where you saved the file using your command line (Terminal, Command Prompt, or PowerShell).

Run the Script: Execute the application using the following command:

python todo_manager.py


Data Persistence

Upon the first run, the application will create a new file named todo_list.txt in the same directory. This file will store your tasks and be used to load them every time the application starts.

🖥️ Application Usage

The manager operates on a simple, looping menu:

View Current List: The list is displayed automatically upon startup and after every action.

Add a new task (Option 1):

Enter 1 and press Enter.

Input the task description when prompted. The task is immediately added and saved.

Remove a task (Option 2):

Enter 2 and press Enter.

Enter the number (index) of the task you want to remove (e.g., enter 1 to remove the first task). The task is removed and saved.

Exit and Save (Option 3):

Enter 3 and press Enter to close the program safely.

⚙️ Code Design Highlights

The program structure is clean and modular, focusing on clear separation of concerns:

DATA_FILE & todo_list: Global variables manage the file path and the in-memory representation of the list.

load_tasks() & save_tasks(): Dedicated functions handle all file input/output (I/O) operations, ensuring data integrity.

add_task() & remove_task(): These functions manage the core logic for manipulating the list, handling validation and immediately triggering a save operation upon successful modification.

main_menu(): Contains the user interaction loop, loading tasks once at the start and offering continuous menu options.

💡 Future Enhancements

The project can be expanded with more advanced features, such as:

Marking Tasks as Complete: Adding a feature to toggle a completion status ([X] Buy milk).

Task Editing: Allowing users to modify the text of an existing task without having to delete and re-add it.

Prioritization: Implementing priority levels (e.g., [HIGH], [LOW]) and sorting the display accordingly.
