from tkinter import simpledialog, messagebox
import csv

def create_new_database(fields):
    """Prompt user to create a new database with a unique file name."""
    try:
        # Ask the user for the name of the new database
        file_name = simpledialog.askstring("New Database", "Enter a unique file name (without extension):")
        if not file_name:  # If the user cancels or doesn't provide a name
            messagebox.showerror("Error", "No file name provided. Database creation canceled.")
            return None, [], []

        file_name = file_name.strip() + ".csv"  # Add `.csv` extension
        with open(file_name, "w", newline="") as f:
            csv.writer(f).writerow(fields)  # Write header fields
        messagebox.showinfo("Success", f"New database '{file_name}' created successfully!")
        return file_name, fields, []  # Return the new file name, fields, and an empty records list
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create new database: {e}")
        return None, [], []
def save_database(file_name, fields, records):
    """Save the database."""
    try:
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(fields)  # Write the header row
            for record in records:
                writer.writerow(record)  # Write each record row
        messagebox.showinfo("Success", "Database saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save database: {e}")
