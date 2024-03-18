from db import c, conn


"""
PK - Primary Key
"""

# employee.py
import sqlite3


class Employee:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def save(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        conn.commit()
        conn.close()

    @classmethod
    def get_list(cls, **kwargs):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        query = "SELECT * FROM employee WHERE "
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)

        query += " AND ".join(conditions)
        c.execute(query, values)

        employees = []
        for row in c.fetchall():
            employees.append(Employee(row['name'], row['surname'], row['age']))

        conn.close()
        return employees

    def delete(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("DELETE FROM employee WHERE name=? AND surname=? AND age=?", (self.name, self.surname, self.age))
        conn.commit()
        conn.close()

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age




