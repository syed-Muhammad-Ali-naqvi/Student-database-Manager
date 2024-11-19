import csv
from tkinter import messagebox

def load_database(file_name):
    """Load an existing database."""
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            fields = next(reader)
            records = [row for row in reader]
        messagebox.showinfo("Success", f"Database '{file_name}' loaded successfully!")
        return fields, records
    except FileNotFoundError:
        messagebox.showerror("Error", f"Database '{file_name}' not found!")
        return [], []

def create_new_database(file_name, fields):
    """Create a new database."""
    try:
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(fields)
        messagebox.showinfo("Success", f"New database '{file_name}' created successfully!")
        return fields, []
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create database: {e}")
        return [], []

def save_database(file_name, fields, records):
    """Save the database."""
    try:
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerows(records)
        messagebox.showinfo("Success", f"Database '{file_name}' saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save database: {e}")
