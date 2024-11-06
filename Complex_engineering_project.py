import csv
import re
from tkinter import *
from tkinter import messagebox, ttk

# ==============================
# Initialize main window
# ==============================
window = Tk()
window.title("Student Database Management")
window.geometry("800x600")

database = []
loaded_database = "student_database.csv"
new_database = "new_database.csv"

# ==============================
# Load and Save Functions
# ==============================

def load_database():
    global database, choice
    choice = 1
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
        choice = 2

def create_database():
    global choice
    choice = 2
    with open(new_database, "w+"):
        pass
    messagebox.showinfo("Info", f"New Database file {new_database} created.")

def save_database():
    filename = loaded_database if choice == 1 else new_database
    with open(filename, "w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(database)
    messagebox.showinfo("Info", "Changes saved successfully.")

# ======================
# Record Functions
# ======================

def validate_roll_number(roll_num):
    if re.match(r"^CP-\d{2}$", roll_num):
        return True
    else:
        messagebox.showerror("Error", "Invalid roll number format. Use 'CP-' followed by exactly 2 digits.")
        return False

def calculate_percentage(quiz_1, quiz_2, mids):
    try:
        return round(((quiz_1 + quiz_2 + mids) * 100)/ 100, 2)
    except (TypeError, ValueError):
        return "N/A"

def add_record():
    roll_num = roll_entry.get()
    name = name_entry.get()
    try:
        quiz_1 = float(quiz_1_entry.get())
        quiz_2 = float(quiz_2_entry.get())
        mids = float(mids_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for quiz and midterm scores.")
        return

    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                messagebox.showwarning("Warning", "Record with this roll number already exists.")
                return

        percentage = calculate_percentage(quiz_1, quiz_2, mids)
        database.append([roll_num, name, quiz_1, quiz_2, mids, percentage])
        messagebox.showinfo("Info", "Record added successfully.")
        save_database()

def search_record():
    roll_no = roll_entry.get()
    if validate_roll_number(roll_no):
        for record in database:
            if record[0] == roll_no:
                display_record(record)
                return
        messagebox.showinfo("Info", "No such record found.")

def edit_record():
    roll_num = roll_entry.get()
    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                try:
                    record[1] = name_entry.get()
                    record[2] = float(quiz_1_entry.get())
                    record[3] = float(quiz_2_entry.get())
                    record[4] = float(mids_entry.get())
                    record[5] = calculate_percentage(record[2], record[3], record[4])
                    messagebox.showinfo("Info", "Record edited successfully.")
                    save_database()
                    return
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers for quiz and midterm scores.")
                    return
        messagebox.showinfo("Info", "No such record found.")

def delete_record():
    roll_num = roll_entry.get()
    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                database.remove(record)
                messagebox.showinfo("Info", "Record deleted successfully.")
                save_database()
                return
        messagebox.showinfo("Info", "No such record found.")

# ======================
# Display Functions
# ======================

def display_record(record):
    text_area.delete("1.0", END)
    text_area.insert(END, f"Roll No.: {record[0]}\nName: {record[1]}\nQuiz 1: {record[2]}\nQuiz 2: {record[3]}\nMids: {record[4]}\nPercentage: {record[5]}\n")

def view_records():
    text_area.delete("1.0", END)
    for record in database:
        text_area.insert(END, "====================\n")
        text_area.insert(END, f"Roll No.: {record[0]}\nName: {record[1]}\nQuiz 1: {record[2]}\nQuiz 2: {record[3]}\nMids: {record[4]}\nPercentage: {record[5]}\n")
        text_area.insert(END, "====================\n")

# ==============================
# GUI Components
# ==============================

button1 = ttk.Button(window, text="Load existing database", command=load_database)
button1.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")
button2 = ttk.Button(window, text="Create a new one", command=create_database)
button2.grid(row=0, column=2, padx=10, pady=10, columnspan=2, sticky="ew")

# Labels and Entries
Label(window, text="Roll no:").grid(row=1, column=0, sticky='e', padx=5)
Label(window, text="Name:").grid(row=2, column=0, sticky='e', padx=5)
Label(window, text="Quiz 1:").grid(row=3, column=0, sticky='e', padx=5)
Label(window, text="Quiz 2:").grid(row=4, column=0, sticky='e', padx=5)
Label(window, text="Mid terms:").grid(row=5, column=0, sticky='e', padx=5)

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

# Buttons for Actions
ttk.Button(window, text="Add record", command=add_record).grid(row=6, column=0, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Search record", command=search_record).grid(row=6, column=1, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Edit record", command=edit_record).grid(row=6, column=2, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Delete record", command=delete_record).grid(row=6, column=3, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="View all records", command=view_records).grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# Text Area for Displaying Records
text_area = Text(window, width=80, height=15)
text_area.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

# Run Application
window.mainloop()
