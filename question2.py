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
