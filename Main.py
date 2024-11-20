from tkinter import Tk, Frame, Text, simpledialog, ttk
from Database_operation import load_database, create_new_database
from Record_operation import view_records, add_record, edit_record, delete_record, search_record
from Display_operation import update_fields, setup_buttons

# ===================
# Global Variables
# ===================
fields = []                                                 # List to store database field names
records = []                                                # List to store database records
database_file = ""                                          # String to store the current database file name
entries = {}                                                # Dictionary to map field names to entry widgets

def main_window():
    global fields, records, database_file, entries

    # ===================
    # Main Window Setup
    # ===================
    window = Tk()
    window.title("Student Database Management System")
    window.geometry("800x600")

    # ===================
    # Frame for Field Entries
    # ===================
    field_frame = Frame(window)
    field_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # ===================
    # Frame for Buttons
    # ===================
    button_frame = Frame(window)
    button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # ===================
    # Text Area for Output
    # ===================
    text_area = Text(window, width=80, height=15)
    text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="news")

    # Configure row and column weights to make the layout responsive
    window.grid_rowconfigure(3, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # ===================
    # Update Interface
    # ===================
    def update_interface():
        """
        Update the interface with the fields and buttons for the loaded or created database.
        """
        update_fields(field_frame, fields, entries)
        setup_buttons(button_frame, text_area, fields, records, database_file, entries)

    # ===================
    # Load Existing Database
    # ===================
    def load_existing_database():
        """
        Load an existing database file.
        """
        global fields, records, database_file
        # Ask the user to provide the name of the database file
        file_name = simpledialog.askstring("Load Database", "Enter the name of the database (without .csv):")
        if file_name:
            database_file = file_name.strip() + ".csv"  # Append the .csv extension
            fields, records = load_database(database_file)  # Load the database
            if fields:  # If fields are loaded successfully, update the interface
                update_interface()

    # ===================
    # Create New Database
    # ===================
    def create_new_database_interface():
        """
        Create a new database file with user-defined fields.
        """
        global fields, records, database_file
        # Ask the user for the new database name
        file_name = simpledialog.askstring("Create Database", "Enter the name for the new database (without .csv):")
        if file_name:
            database_file = file_name.strip() + ".csv"  # Append the .csv extension
            # Ask the user for field names
            fields_input = simpledialog.askstring("Fields", "Enter field names separated by commas:")
            if fields_input:
                fields = [field.strip() for field in fields_input.split(",")]  # Split and clean field names
                fields, records = create_new_database(database_file, fields)  # Create the new database
                update_interface()

    # ===================
    # Buttons for Database Operations
    # ===================
    ttk.Button(window, text="Load Existing Database", command=load_existing_database).grid(
        row=0, column=0, padx=10, pady=10, sticky="ew"
    )
    ttk.Button(window, text="Create New Database", command=create_new_database_interface).grid(
        row=0, column=1, padx=10, pady=10, sticky="ew"
    )

    # ===================
    # Start Main Event Loop
    # ===================
    window.mainloop()

if __name__ == "__main__":
    main_window()
