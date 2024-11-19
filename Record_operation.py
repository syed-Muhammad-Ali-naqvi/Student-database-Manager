from tkinter import messagebox, END

def add_record(fields, records, entries, database_file, text_area):
    values = [entries[field].get().strip() for field in fields]
    if "" in values:
        messagebox.showerror("Error", "All fields must be filled!")
        return
    if any(record[0] == values[0] for record in records):
        messagebox.showerror("Error", f"Roll number '{values[0]}' already exists!")
        return
    records.append(values)
    messagebox.showinfo("Success", "Record added successfully!")
    text_area.insert(END, f"Added Record: {values}\n")

def search_record(fields, records, entries, text_area):
    key = entries[fields[0]].get().strip()
    for record in records:
        if record[0] == key:
            text_area.delete("1.0", END)
            text_area.insert(END, "Record Found:\n")
            for field, value in zip(fields, record):
                text_area.insert(END, f"{field}: {value}\n")
            return
    messagebox.showinfo("Not Found", "No record found with the given key.")

def edit_record(fields, records, entries, database_file, text_area):
    key = entries[fields[0]].get().strip()
    for i, record in enumerate(records):
        if record[0] == key:
            new_values = [entries[field].get().strip() for field in fields]
            if "" in new_values:
                messagebox.showerror("Error", "All fields must be filled!")
                return
            records[i] = new_values
            messagebox.showinfo("Success", "Record updated successfully!")
            text_area.insert(END, f"Updated Record: {new_values}\n")
            return
    messagebox.showerror("Error", "Record not found!")

def delete_record(fields, records, entries, database_file, text_area):
    key = entries[fields[0]].get().strip()
    for i, record in enumerate(records):
        if record[0] == key:
            records.pop(i)
            messagebox.showinfo("Success", f"Record '{key}' deleted!")
            text_area.insert(END, f"Deleted Record: {key}\n")
            return
    messagebox.showerror("Error", "Record not found!")

def view_records(fields, records, text_area):
    text_area.delete("1.0", END)
    for record in records:
        for field, value in zip(fields, record):
            text_area.insert(END, f"{field}: {value}\n")
        text_area.insert(END, f"{'=' * 30}\n")
