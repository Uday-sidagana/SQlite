import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('employee.db')

c= conn.cursor()

def insert_emp(emp):
    with conn:
        c.execute(" INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last': emp.last, 'pay': emp.pay})

def fetch_emp(param, value):
    with conn:
        c.execute(" SELECT * FROM employees WHERE param=:param", {'param': 'value'})
        return c.fetchall()


c.execute(""" CREATE TABLE employees (
          first text,
          last text,
          pay integer)     
           """)

#from employee module
emp1 = Employee('sumit', 'shukla', 1500)
emp2 = Employee('aditya', 'dikhit', 10)
emp3 = Employee('ketchup', 'man', 9999)

c.execute(" INSERT INTO employees VALUES ('{}','{}',{})".format(emp1.first, emp1.last, emp1.pay)) 
c.execute(" INSERT INTO employees VALUES (?,?,?)", (emp2.first, emp2.last, emp2.pay))
c.execute(" INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp3.first, 'last': emp3.last, 'pay': emp3.pay})



c.execute(" INSERT INTO employees VALUES ('uday', 'sidagana', 5000) ")
c.execute(" INSERT INTO employees VALUES ('sam', 'lmao', 3000) ")
c.execute(" INSERT INTO employees VALUES ('jakarta', 'sidagana', 5000) ")

c.execute(" SELECT * FROM employees WHERE last=?", ('sidagana',))
print(c.fetchall())

c.execute(" SELECT * FROM employees WHERE last=:last", {'last': 'man'})
print(c.fetchall())

c.execute(" SELECT * FROM employees ")
print(c.fetchall)
# c.fetchall()
# c.fetchone()
# c.fetchmany(5)


conn.commit()
conn.close()
