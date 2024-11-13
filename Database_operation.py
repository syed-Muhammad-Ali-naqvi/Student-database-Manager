# database_operations.py
# Handles database-related operations, such as loading, creating, and saving records.

import csv
from tkinter import messagebox

# In-memory database list
database = []

# File names for the existing and new databases
loaded_database = "student_database.csv"
new_database = "new_database.csv"

# Default database choice
choice = 1  # 1 for loaded database, 2 for new database

def load_database():
    """Loads data from the existing database file into the in-memory list."""
    global database, choice
    choice = 1  # Indicates existing database is in use
    try:
        with open(loaded_database, "r") as f:
            database.clear()
            reader = csv.reader(f)
            for row in reader:
                if row:
                    database.append(row)
        messagebox.showinfo("Info", "Database loaded successfully!")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No such database found. Starting with a new one.")
        choice = 2  # Switch to new database if file not found

def create_database():
    """Creates a new, empty database file."""
    global choice
    choice = 2  # Indicates new database is in use
    with open(new_database, "w+"):
        pass
    messagebox.showinfo("Info", f"New Database file {new_database} created.")

def save_database():
    """Saves the current in-memory data to the selected database file."""
    filename = loaded_database if choice == 1 else new_database
    with open(filename, "w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(database)
    messagebox.showinfo("Info", "Changes saved successfully.")
