from tkinter import messagebox, END

# ===================
# Record Operations
# ===================


"""
Add a new record to the database.

Parameters:
    fields (list): List of field names.
    records (list): List of current records.
    entries (dict): Dictionary containing user input for each field.
    database_file (str): File name of the database.
    text_area (Text): Text widget to display the result.

"""


# ===================
# Add Record
# ===================
def add_record(fields, records, entries, database_file, text_area):

    values = [entries[field].get().strip() for field in fields]  # Collect input values for all fields
    if "" in values:
        # Error if any field is left blank
        messagebox.showerror("Error", "All fields must be filled!")
        return
    if any(record[0] == values[0] for record in records):
        # Error if the roll number already exists
        messagebox.showerror("Error", f"Roll number '{values[0]}' already exists!")
        return
    records.append(values)  # Add the new record to the records list
    messagebox.showinfo("Success", "Record added successfully!")  # Notify success
    text_area.insert(END, f"Added Record: {values}\n")  # Display the added record in the text area

# ===================
# Search Record
# ===================
def search_record(fields, records, entries, text_area):

    key = entries[fields[0]].get().strip()  # Get the search key from the first field
    for record in records:
        if record[0] == key:  # Match found
            text_area.delete("1.0", END)  # Clear the text area
            text_area.insert(END, "Record Found:\n")  # Display a header
            for field, value in zip(fields, record):
                text_area.insert(END, f"{field}: {value}\n")  # Display each field-value pair
            return
    # Notify user if no matching record is found
    messagebox.showinfo("Not Found", "No record found with the given key.")


# ===================
# Edit Record
# ===================
def edit_record(fields, records, entries, database_file, text_area):

    key = entries[fields[0]].get().strip()  # Get the key to identify the record
    for i, record in enumerate(records):
        if record[0] == key:  # Match found
            new_values = [entries[field].get().strip() for field in fields]  # Get updated values
            if "" in new_values:
                # Error if any field is left blank
                messagebox.showerror("Error", "All fields must be filled!")
                return
            records[i] = new_values  # Update the record
            messagebox.showinfo("Success", "Record updated successfully!")  # Notify success
            text_area.insert(END, f"Updated Record: {new_values}\n")  # Display the updated record
            return
    # Notify user if no matching record is found
    messagebox.showerror("Error", "Record not found!")


# ===================
# Delete Record
# ===================
def delete_record(fields, records, entries, database_file, text_area):

    key = entries[fields[0]].get().strip()  # Get the key to identify the record
    for i, record in enumerate(records):
        if record[0] == key:  # Match found
            records.pop(i)  # Remove the record from the list
            messagebox.showinfo("Success", f"Record '{key}' deleted!")  # Notify success
            text_area.insert(END, f"Deleted Record: {key}\n")  # Display the deletion in the text area
            return
    # Notify user if no matching record is found
    messagebox.showerror("Error", "Record not found!")


# ===================
# View Record
# ===================
def view_records(fields, records, text_area):

    text_area.delete("1.0", END)                                                   # Clear the text area
    for record in records:
        for field, value in zip(fields, record):
            text_area.insert(END, f"{field}: {value}\n")                            # Display each field-value pair
        text_area.insert(END, f"{'=' * 30}\n")                                      # Add a separator between records
