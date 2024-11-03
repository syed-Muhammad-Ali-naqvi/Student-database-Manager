import csv
import re
from tkinter import *
from tkinter import messagebox, ttk


#Initialize main window
window = Tk()
window.title("Student Database Management")
window.geometry("800x600")


database = []
loaded_database = "student_database.csv"
new_database = "new_database.csv"

def load_database():
    global database, choice
    choice = 1
    try:
        with open(loaded_database, "r") as f:
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
    with open(new_database, "a+"):
        pass
    messagebox.showinfo("Info", f"New Database file {new_database} created.")

# for saving changes into database
def save_database():
    global choice
    if choice == 1:
        filename = loaded_database
        with open(loaded_database, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(database)
        print("Changes saved successfully!")
    elif choice == 2:
        with open(new_database, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(database)
        messagebox.showinfo("Info", "Changes saved successfully.")


# Validate roll no.
def validate_roll_number(roll_num):
    #roll_num = input("Enter roll_no. (format CP-##): ")
    if re.match(r"^CP-\d{2}$", roll_num):
        return True
    else:
        messagebox.showerror("Error", "Invalid roll number format. Use 'CP-' followed by exactly 2 digits.")
        return False

# Adding new record
def add_record():
    roll_num = roll_entry.get()
    name = name_entry.get()
    quiz_1 = float(quiz_1_entry.get())
    quiz_2 = float(quiz_2_entry.get())
    mids = float(mids_entry.get())

    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                messagebox.showwarning("Warning", "Record with this roll number already exist")
                return
    percentage = ((quiz_1 + quiz_2 + mids) / 100) * 100 if quiz_1 != "" and quiz_2 != "" and mids != "" else "N/A"
    database.append([roll_num, name, quiz_1, quiz_2, mids, percentage])
    messagebox.showinfo("Info", "Record added successfully")
    save_database()



# Searching for record

def search_record():
    roll_no = roll_entry.get()
    if validate_roll_number((roll_no)):
        for record in database:
            if record[0] == roll_no:
                display_record(record)
                return
        messagebox.showinfo("Info", "No such record found")



# Editing record
def edit_record():
    roll_num = roll_entry.get()
    if validate_roll_number(roll_num):
        for record in database:
            if roll_num == record[0]:
                record[1] = name_entry.get()
                record[2] = float(quiz_1_entry.get())
                record[3] = float(quiz_2_entry.get())
                record[4] = float(mids_entry.get())
                messagebox.showinfo("Info", "Record edited successfully")
                save_database()
                return
        else:
            messagebox.showinfo("Info", "No such record found")


# Delete a record
def delete_record():
    roll_num = roll_entry.get()
    if validate_roll_number(roll_num):
        for record in database:
            if record[0] == roll_num:
                database.remove(record)
                messagebox.showinfo("Info", "Record deleted suuccessfully")
                save_database()
                return
        messagebox.showinfo("Info", "No such record found")

# Display single record
def display_record(record):
    text_area.delete("1.0", END)
    text_area.insert(END, f"Roll No.: {record[0]}\nName: {record[1]}\nQuiz_1: {record[2]}\nQuiz_2: {record[3]}\nMids: {record[4]}\nPercentage: {record[5]}\n")

# Show database
def view_records():
    text_area.delete("1.0", END)
    for record in database:
        text_area.insert(END, f"====================\n")
        text_area.insert(END, f"Roll No.: {record[0]}\nName: {record[1]}\nQuiz_1: {record[2]}\nQuiz_2: {record[3]}\nMids: {record[4]}\nPercentage: {record[5]}\n")
        text_area.insert(END, f"====================\n")

# GUI components
# Buttons for database options

button1 = ttk.Button(window,text="Load existing database", command=load_database)
button1.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")
button2 = ttk.Button(window, text="Create a new one", command=create_database)
button2.grid(row=0, column=2, padx=10, pady=10, columnspan=2, sticky="ew")

## Now creating buttons for fields
Label(window, text="Roll no: ").grid(row=1, column=0, sticky='e', padx=5)
Label(window, text="Name:").grid(row=2, column=0, sticky='e', padx=5)
Label(window, text="Quiz_1:").grid(row=3, column=0, sticky='e', padx=5)
Label(window, text="Quiz_2:").grid(row=4, column=0,sticky='e', padx=5)
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


## Buttons for fields
ttk.Button(window, text="Add record", command=add_record).grid(row=6, column=0, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Search record", command=search_record).grid(row=6, column=1, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Edit record", command=edit_record).grid(row=6, column=2, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="Delete record", command=delete_record).grid(row=6, column=3, padx=5, pady=10, sticky='ew')
ttk.Button(window, text="View all records", command=view_records).grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky='ew')


# Text area to display database and records
text_area = Text(window, width=80, height=15)
text_area.grid(row=8, column=0, columnspan=4, padx=10, pady=10)


## Finally running the application
window.mainloop()
