# display_operations.py
# Manages functions for displaying individual and all records in the text area.

from tkinter import END

def display_record(record, text_area):
    """Clears and displays a single record in the provided text area widget."""
    text_area.delete("1.0", END)
    text_area.insert(END, f"Roll No.: {record[0]}\nName: {record[1]}\nQuiz 1: {record[2]}\nQuiz 2: {record[3]}\nMids: {record[4]}\nPercentage: {record[5]}\n")

def view_records(database, text_area):
    """Clears and displays all records in the provided text area widget."""
    text_area.delete("1.0", END)
    for record in database:
        text_area.insert(END, "====================\n")
        text_area.insert(END, f"Roll No.: {record[0]}\nName: {record[1]}\nQuiz 1: {record[2]}\nQuiz 2: {record[3]}\nMids: {record[4]}\nPercentage: {record[5]}\n")
        text_area.insert(END, "====================\n")
