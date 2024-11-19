from tkinter import messagebox, END
from Database_operation import save_database


# Add a record
def add_record(fields, records, entries, database_file, text_area):
    # Collect field values from entries
    values = [entries[field].get().strip() for field in fields]

    # Check for empty fields
    if "" in values:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    # Check for duplicate roll numbers (first field)
    roll_number = values[0]  # Assuming the first field is the unique identifier
    for record in records:
        if record[0] == roll_number:
            messagebox.showerror("Error", f"Roll number '{roll_number}' already exists!")
            return

    # Add values to records and save
    records.append(values)
    save_database(database_file, fields, records)
    messagebox.showinfo("Success", "Record added!")

    # Display added record
    text_area.insert(END, f"Added Record: {values}\n")

# Search for a record
def search_record(fields, records, entries, text_area):
    # Get the search key from the first field
    key = entries[fields[0]].get().strip()

    # Find the record with the matching key
    for record in records:
        if record[0] == key:
            text_area.delete("1.0", END)
            text_area.insert(END, "Record Found:\n")

            # Show each field and value
            for field, value in zip(fields, record):
                text_area.insert(END, f"{field}: {value}\n")
            return

    # If no record is found
    messagebox.showinfo("Not Found", "No record found with the given key.")


# Edit a record
def edit_record(fields, records, entries, database_file, text_area):
    # Get the search key from the first field
    key = entries[fields[0]].get().strip()

    # Look for the record to update
    for i, record in enumerate(records):
        if record[0] == key:
            # Collect updated values
            new_values = [entries[field].get().strip() for field in fields]

            # Check for empty fields
            if "" in new_values:
                messagebox.showerror("Error", "All fields must be filled!")
                return

            # Update record and save changes
            records[i] = new_values
            save_database(database_file, fields, records)
            messagebox.showinfo("Success", "Record updated!")

            # Show updated record
            text_area.insert(END, f"Updated Record: {new_values}\n")
            return

    # If no record is found
    messagebox.showerror("Error", "Record not found!")


# Delete a record
def delete_record(fields, records, entries, database_file, text_area):
    # Get the search key from the first field
    key = entries[fields[0]].get().strip()

    # Find and delete the record
    for i, record in enumerate(records):
        if record[0] == key:
            records.pop(i)
            save_database(database_file, fields, records)
            messagebox.showinfo("Success", "Record deleted!")

            # Show confirmation
            text_area.insert(END, f"Deleted Record with Key: {key}\n")
            return

    # If no record is found
    messagebox.showerror("Error", "Record not found!")


# View all records
def view_records(fields, records, text_area):
    # Clear the text area before displaying records
    text_area.delete("1.0", END)

    # Display each record
    for record in records:
        for field, value in zip(fields, record):
            text_area.insert(END, f"{field}: {value}\n")
        text_area.insert(END, "=" * 30 + "\n")
