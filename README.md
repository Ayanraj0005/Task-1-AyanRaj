# 📝 DecodeLabs To-Do Engine

A simple command-line To-Do List application built with Python that allows users to manage tasks and store them permanently using JSON file persistence.

## 🚀 Features

- Add new tasks
- View all saved tasks
- Automatic data persistence using JSON
- Loads existing tasks when the application starts
- Simple and beginner-friendly command-line interface
- Modular code structure with separate data and UI logic

---

## 📂 Project Structure

```
TO_DO_LIST/
│
├── To_do_list_1.py      # Main application
├── tasks.json           # Stores tasks permanently
└── README.md            # Project documentation
```

---

## 🛠️ Technologies Used

- Python 3
- JSON
- OS Module

---

## ⚙️ How It Works

### 1. Application Startup

When the application starts, it automatically loads tasks from `tasks.json`.

```python
load_tasks()
```

If the file does not exist, an empty task list is created.

---

### 2. Add a Task

Select:

```
1. Add a Task
```

Enter the task description:

```
Enter the task description: Complete Python Project
```

The task is:

- Added to memory
- Saved instantly to `tasks.json`

---

### 3. View Tasks

Select:

```
2. View Tasks
```

Example Output:

```
CURRENT TASKS:
[0] Complete the Homework.
[1] Buy milk.
[2] code practice.
[3] PLAY CRICKET
[4] DO HOMEWORK
[5] go to school
```

---

### 4. Exit

Select:

```
3. Exit
```

Output:

```
Terminating process. Goodbye!
```

---

## 📄 Example Menu

```
--- DecodeLabs To-Do Engine ---
1. Add a Task
2. View Tasks
3. Exit
```

---

## 💾 Data Persistence

Tasks are stored inside:

```json
[
    "Complete the Homework.",
    "Buy milk.",
    "code practice.",
    "PLAY CRICKET",
    "DO HOMEWORK",
    "go to school"
]
```

This ensures tasks remain available even after closing the program.

---

## 🧩 Functions Overview

| Function | Purpose |
|-----------|---------|
| `load_tasks()` | Loads tasks from JSON file |
| `save_tasks()` | Saves tasks to JSON file |
| `add_task()` | Adds a new task |
| `get_tasks()` | Returns all tasks |
| `show_menu()` | Displays the main menu |
| `display_tasks()` | Prints all tasks |
| `main()` | Controls application flow |

---

## ▶️ Running the Project

### Clone the Repository

```bash
git clone https://github.com/yourusername/decodeLabs-todo-engine.git
```

### Navigate to Project Folder

```bash
cd decodeLabs-todo-engine
```

### Run the Application

```bash
python3 To_do_list_1.py
```

---

## 📈 Future Improvements

- Delete tasks
- Mark tasks as completed
- Task priorities
- Due dates
- Search functionality
- GUI version using Tkinter
- Database integration (SQLite)

---

## 🎯 Learning Concepts Demonstrated

- Functions
- Lists
- File Handling
- JSON Serialization & Deserialization
- Data Persistence
- Command-Line Interfaces (CLI)
- Modular Programming

---

## 👨‍💻 Author

Raj Ayan

Built as a Python learning project to demonstrate task management and persistent storage using JSON.
