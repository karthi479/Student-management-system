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


           