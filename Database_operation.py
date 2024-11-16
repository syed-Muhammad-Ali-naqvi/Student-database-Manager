import csv
from tkinter import messagebox

# Load an existing database
def load_database(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            fields = next(reader)  # Read the header row
            records = list(reader)  # Read the remaining rows
        return fields, records
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_name} not found!")
        return [], []

# Create a new database
def create_new_database(file_name, fields):
    try:
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(fields)  # Write the header row
        return fields, []  # Return empty records
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create database: {e}")
        return [], []

# Save the database
def save_database(file_name, fields, records):
    try:
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(fields)  # Write the header row
            writer.writerows(records)  # Write the records
        messagebox.showinfo("Success", "Database saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save database: {e}")
