## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Main Menu](#main-menu)
  - [Adding Tasks](#adding-tasks)
  - [Viewing Tasks](#viewing-tasks)
  - [Marking Tasks as Complete](#marking-tasks-as-complete)
  - [Clearing Completed Tasks](#clearing-completed-tasks)
  - [Exit Program](#exit-program)
- [Data Persistence](#data-persistence)

## Getting Started

### Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download) must be installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-todo-list.git
   
2. Navigate to the project directory:

   ```bash
   cd your-todo-list
   
3. Build and run the application:

   ```bash
   dotnet run
   
## Usage

### Main Menu

To-Do List Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Clear Completed Tasks
5. Exit

### Adding Tasks

Choose option 1 to add a new task.
Enter the task name when prompted.
The task will be added to the list of tasks.

### Viewing Tasks

Select option 2 to view all tasks.
The tasks will be displayed with their completion status.

### Marking Tasks as Complete

Choose option 3 to mark a task as complete.
You'll be prompted to enter the task number to mark.
The selected task will be marked as complete.

### Clearing Completed Tasks

Select option 4 to clear all completed tasks from the list.
All completed tasks will be removed.

### Exit Program

Select option 5 to exit the program.

## Data Persistence

Your tasks are saved to a text file named todolist.txt. This allows your to-do list data to persist between program runs.

