from tkinter import Label, Entry, ttk
from Record_operation import add_record, delete_record, edit_record, search_record, view_records

# ====================
# Update Fields Section
# ====================

def update_fields(frame, fields, entries):
    """
    Dynamically create input fields for the database records.

    Parameters:
        frame (Frame): The parent frame where fields will be displayed.
        fields (list): List of field names for the records.
        entries (dict): Dictionary to store the Entry widgets for user input.

    Returns:
        None
    """
    # Clear any existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()
    # Clear the entries dictionary
    entries.clear()

    # Loop through each field to create labels and entry widgets
    for i, field in enumerate(fields):
        # Create a label for the field
        Label(frame, text=f"{field}:").grid(row=i, column=0, padx=5, pady=5, sticky="e")
        # Create an entry widget for user input
        entry = Entry(frame)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
        # Store the entry widget in the entries dictionary
        entries[field] = entry

# ======================
# Setup Buttons Section
# =====================

def setup_buttons(frame, text_area, fields, records, database_file, entries):
    """
    Setup the operation buttons for record management.

    Parameters:
        frame (Frame): The parent frame where buttons will be displayed.
        text_area (Text): Text widget for displaying results or messages.
        fields (list): List of field names for the records.
        records (list): List of current records in the database.
        database_file (str): Name of the database file.
        entries (dict): Dictionary to store the Entry widgets for user input.

    Returns:
        None
    """
    # Clear any existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Create and grid buttons for various operations
    ttk.Button(
        frame,
        text="Add Record",
        command=lambda: add_record(fields, records, entries, database_file, text_area)
    ).grid(row=0, column=0, padx=5, pady=5)

    ttk.Button(
        frame,
        text="Search Record",
        command=lambda: search_record(fields, records, entries, text_area)
    ).grid(row=0, column=1, padx=5, pady=5)

    ttk.Button(
        frame,
        text="Edit Record",
        command=lambda: edit_record(fields, records, entries, database_file, text_area)
    ).grid(row=0, column=2, padx=5, pady=5)

    ttk.Button(
        frame,
        text="Delete Record",
        command=lambda: delete_record(fields, records, entries, database_file, text_area)
    ).grid(row=0, column=3, padx=5, pady=5)

    ttk.Button(
        frame,
        text="View All Records",
        command=lambda: view_records(fields, records, text_area)
    ).grid(row=0, column=4, padx=5, pady=5)
