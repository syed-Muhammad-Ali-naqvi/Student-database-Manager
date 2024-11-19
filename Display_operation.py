from tkinter import Label, Entry, ttk
from Record_operation import add_record, delete_record, edit_record, search_record, view_records
def update_fields(frame, fields, entries):
    for widget in frame.winfo_children():
        widget.destroy()
    entries.clear()
    for i, field in enumerate(fields):
        Label(frame, text=f"{field}:").grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry = Entry(frame)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
        entries[field] = entry

def setup_buttons(frame, text_area, fields, records, database_file, entries):
    for widget in frame.winfo_children():
        widget.destroy()
    ttk.Button(frame, text="Add Record", command=lambda: add_record(fields, records, entries, database_file, text_area)).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(frame, text="Search Record", command=lambda: search_record(fields, records, entries, text_area)).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(frame, text="Edit Record", command=lambda: edit_record(fields, records, entries, database_file, text_area)).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(frame, text="Delete Record", command=lambda: delete_record(fields, records, entries, database_file, text_area)).grid(row=0, column=3, padx=5, pady=5)
    ttk.Button(frame, text="View All Records", command=lambda: view_records(fields, records, text_area)).grid(row=0, column=4, padx=5, pady=5)
