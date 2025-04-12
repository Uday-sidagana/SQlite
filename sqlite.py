import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

c= conn.cursor()

# c.execute(""" CREATE TABLE employees (
#           first text,
#           last text,
#           pay integer)     
#            """)

# c.execute(" INSERT INTO employees VALUES ('uday', 'sidagana', 5000) ")

c.execute(" SELECT * FROM employees WHERE first='uday' ")

# c.fetchall()
# c.fetchone()
# c.fetchmany(5)
print(c.fetchone())

conn.commit()
conn.close()
