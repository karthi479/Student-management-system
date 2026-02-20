#main.py
import sqlite3
from tabulate import tabulate

#-------------DATABASE SETUP-----------------
# Connect to database (creates file if not exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    marks REAL,
    address TEXT,
    email TEXT UNIQUE
)
""")
conn.commit()

#------------CRUD FUNCTIONS--------------
def add_student(name, age, marks, address, email):
    try:
        cursor.execute("""
        INSERT INTO students (name, age, marks, address, email)
        VALUES (?, ?, ?, ?, ?)
        """, (name, age, marks, address, email))
        conn.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    if rows:
        headers = ["ID", "Name", "Age", "Marks", "Address", "Email"]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No students found.")


def update_student(student_id, name=None, age=None, marks=None, address=None, email=None):
    updates = []
    params = []

    if name:
        updates.append("name = ?")
        params.append(name)
    if age:
        updates.append("age = ?")
        params.append(age)
    if marks:
        updates.append("marks = ?")
        params.append(marks)
    if address:
        updates.append("address = ?")
        params.append(address)
    if email:
        updates.append("email = ?")
        params.append(email)

    params.append(student_id)
    query = f"UPDATE students SET {', '.join(updates)} WHERE id = ?"
    cursor.execute(query, tuple(params))
    conn.commit()
    print("Student updated successfully.")


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Student deleted successfully.")

#-----------------MENU------------------
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            marks = float(input("Marks: "))
            address = input("Address: ")
            email = input("Email: ")
            add_student(name, age, marks, address, email)

        elif choice == '2':
            view_students()

        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            print("Leave blank if no change")
            name = input("Name: ") or None
            age = input("Age: ")
            age = int(age) if age else None
            marks = input("Marks: ")
            marks = float(marks) if marks else None
            address = input("Address: ") or None
            email = input("Email: ") or None
            update_student(student_id, name, age, marks, address, email)

        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


#-------------RUN PROGRAM----------------
if __name__ =="__main__":
    menu()
conn.close()