from tkinter import Tk, Frame, Button, Text, simpledialog
from Database_operation import load_database, create_new_database
from Record_operation import view_records, add_record, edit_record, delete_record, search_record
from Display_operation import update_fields, setup_buttons

fields = []
records = []
database_file = ""
entries = {}

def main_window():
    global fields, records, database_file, entries

    window = Tk()
    window.title("Student Database Management System")
    window.geometry("800x600")

    field_frame = Frame(window)
    field_frame.pack(pady=10)

    button_frame = Frame(window)
    button_frame.pack(pady=10)

    text_area = Text(window, width=80, height=15)
    text_area.pack(pady=10)

    def update_interface():
        update_fields(field_frame, fields, entries)
        setup_buttons(button_frame, text_area, fields, records, database_file, entries)

    def load_existing_database():
        global fields, records, database_file
        database_file = "student_database.csv"
        fields, records = load_database(database_file)
        if fields:
            update_interface()

    def create_new_database_interface():
        global fields, records, database_file
        database_file = "new_database.csv"
        fields_input = simpledialog.askstring("Fields", "Enter field names separated by commas:")
        if fields_input:
            fields = [field.strip() for field in fields_input.split(",")]
            fields, records = create_new_database(database_file, fields)
            update_interface()

    Button(window, text="Load Existing Database", command=load_existing_database).pack(pady=5)
    Button(window, text="Create New Database", command=create_new_database_interface).pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main_window()