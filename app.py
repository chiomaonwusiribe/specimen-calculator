from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to create table (only once)
def init_db():
    conn = sqlite3.connect("specimen_data.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS Specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            microscope_size REAL NOT NULL,
            magnification REAL NOT NULL,
            actual_size REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Call the function when app starts
init_db()

# Save data to database
def save_to_db(username, microscope_size, magnification, actual_size):
    conn = sqlite3.connect("specimen_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO Specimens (username, microscope_size, magnification, actual_size) VALUES (?, ?, ?, ?)",
              (username, microscope_size, magnification, actual_size))
    conn.commit()
    conn.close()

# Main route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        microscope_size = float(request.form['microscope_size'])
        magnification = float(request.form['magnification'])
        actual_size = microscope_size / magnification

        # Save result to DB
        save_to_db(username, microscope_size, magnification, actual_size)

        return render_template('result.html', actual_size=actual_size)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
