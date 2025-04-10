import tkinter as tk
from tkinter import messagebox

import sqlite3



def calculate_actual_size(microscope_size, magnification):
    return microscope_size / magnification

# Example usage
microscope_size = float(input("Enter microscope size (e.g. 5.0 mm): "))
magnification = float(input("Enter magnification (e.g. 100x): "))
actual_size = calculate_actual_size(microscope_size, magnification)
print(f"Actual size of the specimen is {actual_size:.4f} mm")

#Database table
conn = sqlite3.connect("specimen_data.db")
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS Specimens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        microscope_size REAL,
        magnification REAL,
        actual_size REAL
    )
''')

def save_to_db(username, microscope_size, magnification, actual_size):
    c.execute("INSERT INTO Specimens (username, microscope_size, magnification, actual_size) VALUES (?, ?, ?, ?)",
              (username, microscope_size, magnification, actual_size))
    conn.commit()

# Example usage
username = input("Enter your username: ")
microscope_size = float(input("Enter microscope size (mm): "))
magnification = float(input("Enter magnification: "))
actual_size = calculate_actual_size(microscope_size, magnification)

save_to_db(username, microscope_size, magnification, actual_size)
print("Data saved successfully.")

def calculate_and_save():
    try:
        username = entry_username.get()
        microscope_size = float(entry_size.get())
        magnification = float(entry_magnification.get())
        actual_size = microscope_size / magnification
        save_to_db(username, microscope_size, magnification, actual_size)
        messagebox.showinfo("Result", f"Actual Size: {actual_size:.4f} mm\nSaved to database.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

root = tk.Tk()
root.title("Microscope Specimen Calculator")

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Label(root, text="Microscope Size (mm)").grid(row=1, column=0)
tk.Label(root, text="Magnification").grid(row=2, column=0)

entry_username = tk.Entry(root)
entry_size = tk.Entry(root)
entry_magnification = tk.Entry(root)

entry_username.grid(row=0, column=1)
entry_size.grid(row=1, column=1)
entry_magnification.grid(row=2, column=1)

tk.Button(root, text="Calculate & Save", command=calculate_and_save).grid(row=3, columnspan=2)

root.mainloop()