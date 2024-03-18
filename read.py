# Read and display all records from the employee database

import sqlite3


def read_employee_database():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employee")
    rows = c.fetchall()
    conn.close()

    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Surname:", row[2])
        print("Age:", row[3])
        print("\n")


if __name__ == "__main__":
    read_employee_database()
