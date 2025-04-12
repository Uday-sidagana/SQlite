import sqlite3
from employee import Employee

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

c= conn.cursor()

#from employee module
emp1 = Employee('sumit', 'shukla', 1500)
emp2 = Employee('aditya', 'dikhit', 10)

print(emp1.first)
print(emp1.last)
print(emp1.pay)


# c.execute(""" CREATE TABLE employees (
#           first text,
#           last text,
#           pay integer)     
#            """)

# c.execute(" INSERT INTO employees VALUES ('uday', 'sidagana', 5000) ")
# c.execute(" INSERT INTO employees VALUES ('sam', 'lmao', 3000) ")
# c.execute(" INSERT INTO employees VALUES ('jakarta', 'sidagana', 5000) ")

c.execute(" SELECT * FROM employees WHERE last='sidagana' ")

# c.fetchall()
# c.fetchone()
# c.fetchmany(5)
print(c.fetchall())

conn.commit()
conn.close()
