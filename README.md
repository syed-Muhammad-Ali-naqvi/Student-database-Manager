# Student Database Management System

This project is a **Student Database Management System** built using Python's **Tkinter** module for the graphical interface and the **CSV** module for database storage. It allows users to create, load, and manage student databases interactively. The system supports adding, searching, editing, deleting, and viewing student records.

---

## Features
- **Password Protection**: The application starts with a password validation. The user must enter the correct password ("itssecret") to access the system.
- **Create New Databases**: Users can create new databases with custom field names.
- **Load Existing Databases**: Displays a list of all available databases in the current directory for easy loading.
- **Available Files**: "student_database.csv" & "Existing_database.csv"
- **Add Records**: Add new student records to the database.
- **Search Records**: Search for a student using a unique key (e.g., roll number).
- **Edit Records**: Modify existing student records.
- **Delete Records**: Remove a record from the database.
- **View All Records**: Display all records in the database in a readable format.
- **Save Data**: Automatically saves data to CSV files for persistence.

---

## File Structure

### 1. **main_window.py**
   - Handles the main interface of the application.
   - Includes options to load an existing database or create a new one.
   - Displays buttons and a text area for interaction.

### 2. **Database_operation.py**
   - Functions to handle database-related tasks:
     - Load an existing database.
     - Create a new database.
     - Save data to the database.

### 3. **Record_operation.py**
   - Functions to perform CRUD operations on student records:
     - Add a record.
     - Search for a record.
     - Edit a record.
     - Delete a record.
     - View all records.

### 4. **Display_operation.py**
   - Functions to update the GUI dynamically:
     - Update input fields based on database fields.
     - Setup action buttons (Add, Edit, Delete, etc.).

---

## How to Run

1. Ensure you have **Python 3.x** installed.
2. Run `Main.py` to start the application
3. Enter "itssecret" as a password to get access to the system.

---
## Sample Run
1. Start the application by running the script.
2. Enter the password ("itssecret") to proceed.
3. Choose to either load an existing database or create a new one.
4. Perform CRUD operations on the database records (Add, Edit, Delete, View).
