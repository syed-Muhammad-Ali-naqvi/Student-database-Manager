from tkinter import messagebox, END
from Database_operation import save_database

# Add a record
def add_record(fields, records, entries, database_file, text_area):
    values = [entries[field].get() for field in fields]
    if len(values) != len(fields) or "" in values:
        messagebox.showerror("Error", "Please fill all fields correctly!")
        return

    records.append(values)
    save_database(database_file, fields, records)
    messagebox.showinfo("Success", "Record added successfully!")
    text_area.insert(END, f"Added Record: {values}\n")

# Search for a record
def search_record(fields, records, entries, text_area):
    key_value = entries[fields[0]].get()
    for record in records:
        if record[0] == key_value:
            text_area.delete("1.0", END)
            text_area.insert(END, f"Record Found:\n")
            for field, value in zip(fields, record):
                text_area.insert(END, f"{field}: {value}\n")
            return
    messagebox.showinfo("Not Found", "No record found with the given key.")

# Edit a record
def edit_record(fields, records, entries, database_file, text_area):
    key_value = entries[fields[0]].get()
    for i, record in enumerate(records):
        if record[0] == key_value:
            new_values = [entries[field].get() for field in fields]
            if len(new_values) != len(fields) or "" in new_values:
                messagebox.showerror("Error", "Please fill all fields correctly!")
                return
            records[i] = new_values
            save_database(database_file, fields, records)
            messagebox.showinfo("Success", "Record updated successfully!")
            text_area.insert(END, f"Updated Record: {new_values}\n")
            return
    messagebox.showerror("Error", "Record not found!")

# Delete a record
def delete_record(fields, records, entries, database_file, text_area):
    key_value = entries[fields[0]].get()
    for i, record in enumerate(records):
        if record[0] == key_value:
            records.pop(i)
            save_database(database_file, fields, records)
            messagebox.showinfo("Success", "Record deleted successfully!")
            text_area.insert(END, f"Deleted Record with Key: {key_value}\n")
            return
    messagebox.showerror("Error", "Record not found!")

# View all records
def view_records(fields, records, text_area):
    text_area.delete("1.0", END)
    for record in records:
        for field, value in zip(fields, record):
            text_area.insert(END, f"{field}: {value}\n")
        text_area.insert(END, f"{'=' * 30}\n")
