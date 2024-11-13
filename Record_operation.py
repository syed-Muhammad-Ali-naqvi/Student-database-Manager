# record_operations.py
# Contains functions for validating, adding, editing, deleting, and searching student records.

import re
from tkinter import messagebox
from Database_operation import database, save_database

def validate_roll_number(roll_num):
    """Validates the roll number format as 'CP-XX' where XX are two digits."""
    if re.match(r"^CP-\d{2}$", roll_num):
        return True
    else:
        messagebox.showerror("Error", "Invalid roll number format. Use 'CP-' followed by exactly 2 digits.")
        return False

def calculate_percentage(quiz_1, quiz_2, mids):
    """Calculates and returns the percentage based on given quiz and midterm scores."""
    try:
        return round((((quiz_1 + quiz_2 + mids) * 100 )/ 100), 2)
    except (TypeError, ValueError):
        return "N/A"

def add_record(roll_num, name, quiz_1, quiz_2, mids):
    """Adds a new record to the database if the roll number is valid and unique."""
    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                messagebox.showwarning("Warning", "Record with this roll number already exists.")
                return

        percentage = calculate_percentage(quiz_1, quiz_2, mids)
        database.append([roll_num, name, quiz_1, quiz_2, mids, percentage])
        messagebox.showinfo("Info", "Record added successfully.")
        save_database()

def search_record(roll_no, display_callback):
    """Searches for a record by roll number and uses a callback to display it if found."""
    if validate_roll_number(roll_no):
        for record in database:
            if record[0] == roll_no:
                display_callback(record)
                return
        messagebox.showinfo("Info", "No such record found.")

def edit_record(roll_num, name, quiz_1, quiz_2, mids):
    """Edits an existing record's details if found by roll number."""
    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                record[1] = name
                record[2] = quiz_1
                record[3] = quiz_2
                record[4] = mids
                record[5] = calculate_percentage(quiz_1, quiz_2, mids)
                messagebox.showinfo("Info", "Record edited successfully.")
                save_database()
                return
        messagebox.showinfo("Info", "No such record found.")

def delete_record(roll_num):
    """Deletes a record by roll number if it exists in the database."""
    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                database.remove(record)
                messagebox.showinfo("Info", "Record deleted successfully.")
                save_database()
                return
        messagebox.showinfo("Info", "No such record found.")
