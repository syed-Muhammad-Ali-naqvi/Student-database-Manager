# main.py
# The main script that sets up the GUI and integrates all functionality.

from tkinter import *
from tkinter import messagebox, ttk
from Database_operation import load_database, create_database, database
from Record_operation import add_record, search_record, edit_record, delete_record
from Display_operation import display_record, view_records

# Initialize main window
window = Tk()
window.title("Student Database Management")
window.geometry("700x580")

# Buttons for database operations
button1 = ttk.Button(window, text="Load existing database", command=load_database)
button1.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")
button2 = ttk.Button(window, text="Create a new one", command=create_database)
button2.grid(row=0, column=2, padx=10, pady=10, columnspan=2, sticky="ew")

# Labels and input fields
Label(window, text="Roll no:").grid(row=1, column=0, sticky='e', padx=5)
Label(window, text="Name:").grid(row=2, column=0, sticky='e', padx=5)
Label(window, text="Quiz 1:").grid(row=3, column=0, sticky='e', padx=5)
Label(window, text="Quiz 2:").grid(row=4, column=0, sticky='e', padx=5)
Label(window, text="Mid terms:").grid(row=5, column=0, sticky='e', padx=5)

# Entry fields for input
roll_entry = Entry(window)
name_entry = Entry(window)
quiz_1_entry = Entry(window)
quiz_2_entry = Entry(window)
mids_entry = Entry(window)

roll_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=3, sticky='w')
name_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=3, sticky='w')
quiz_1_entry.grid(row=3, column=1, padx=10, pady=5, columnspan=3, sticky='w')
quiz_2_entry.grid(row=4, column=1, padx=10, pady=5, columnspan=3, sticky='w')
mids_entry.grid(row=5, column=1, padx=10, pady=5, columnspan=3, sticky='w')

# Text area for displaying records
text_area = Text(window, width=80, height=15)
text_area.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

# Buttons for record actions
ttk.Button(window, text="Add record", command=lambda: add_record(roll_entry.get(), name_entry.get(), float(quiz_1_entry.get()), float(quiz_2_entry.get()), float(mids_entry.get()))).grid(row=6, column=0, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Search record", command=lambda: search_record(roll_entry.get(), lambda rec: display_record(rec, text_area))).grid(row=6, column=1, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Edit record", command=lambda: edit_record(roll_entry.get(), name_entry.get(), float(quiz_1_entry.get()), float(quiz_2_entry.get()), float(mids_entry.get()))).grid(row=6, column=2, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Delete record", command=lambda: delete_record(roll_entry.get())).grid(row=6, column=3, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="View all records", command=lambda: view_records(database, text_area)).grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# Start the main GUI loop
window.mainloop()
