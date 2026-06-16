import json
import os

# ==========================================
# MODEL: DATA LOGIC & PERSISTENCE
# ==========================================

DATA_FILE = "tasks.json"
my_tasks = []

def load_tasks():
    """Loads tasks from the JSON file into memory when the app starts."""
    global my_tasks
    # Check if the file exists before trying to read it
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            my_tasks = json.load(file) # Deserialization: JSON -> Python List
    else:
        my_tasks = []

def save_tasks():
    """Saves the current state of memory into the JSON file."""
    with open(DATA_FILE, "w") as file:
        # Serialization: Python List -> JSON text
        # indent=4 makes the JSON file human-readable
        json.dump(my_tasks, file, indent=4) 

def add_task(task_name):
    """Appends a new task and immediately saves it to disk."""
    my_tasks.append(task_name)
    save_tasks() # Ensure persistence after every modification

def get_tasks():
    """Returns the current state of the to-do list."""
    return my_tasks

# ==========================================
# VIEW & API BOUNDARY: USER INTERFACE
# ==========================================

def show_menu():
    print("\n--- DecodeLabs To-Do Engine ---")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Exit")
    
def display_tasks():
    tasks = get_tasks()
    
    print("\nCURRENT TASKS:")
    if not tasks:
        print("No tasks found. Your list is empty.")
    else:
        for index, task in enumerate(tasks):
            print(f"[{index}] {task}")

def main():
    # 1. Boot up sequence: Load existing data into memory
    load_tasks()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            new_task = input("Enter the task description: ")
            add_task(new_task)
            print(f"SUCCESS: '{new_task}' added and saved to disk.")
            
        elif choice == '2':
            display_tasks()
            
        elif choice == '3':
            print("Terminating process. Goodbye!")
            break
            
        else:
            print("ERROR: Invalid input. Please select 1, 2, or 3.")

# The Gatekeeper
if __name__ == "__main__":
    main()