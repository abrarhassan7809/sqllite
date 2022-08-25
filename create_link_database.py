import sqlite3
from sqlite3 import IntegrityError
from create_database_demo1 import Employee

conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("""Create TABLE IF NOT EXISTS employee (
        employeeID integer primary key,
        first text not null unique,
        last text not null,
        pay integer not null
    )""")

# ----------------------------

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee (first, last, pay) VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emp_by_name(name):
    c.execute("SELECT * FROM employee WHERE first=:first", {'first': name})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("UPDATE employee SET employeeID = :employeeID pay = :pay WHERE first = :first AND last = :last",
                  {'employeeID': emp.employeeID, 'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employee WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


print("Remove any employee press 3 : ")
print("Add any employee press 2 : ")
print("Show employees List press 1 : ")
user_name = input("Enter Your Choice : ")

if user_name == '3':
    user_first = input("Enter First Name : ")
    user_last = input("Enter Last Name : ")
    user_pay = int(input("Enter The Employee Pay : "))
    emp_1 = Employee(user_first, user_last, user_pay)
    remove_emp(emp_1)
    conn.close()
elif user_name == '2':
    user_first = input("Enter First Name : ")
    user_last = input("Enter Last Name : ")
    user_pay = int(input("Enter The Employee Pay : "))
    emp_1 = Employee(user_first, user_last, user_pay)
    try:
        insert_emp(emp_1)
        conn.close()
    except IntegrityError:
        print("This Employee already exist")
        exit()
elif user_name == '1':
    c.execute("SELECT * FROM employee")
    print(c.fetchall())
    conn.close()
else:
    exit()

conn.close()
# ------------------------

# user_first = input("Enter First Name : ")
# user_last = input("Enter Last Name : ")
# user_pay = int(input("Enter The Employee Pay : "))
#
# emp_1 = Employee(user_first, user_last, user_pay)
#
# try:
#     insert_emp(emp_1)
# except IntegrityError:
#     print("This Employee already exist")
#     pass

# emps = get_emp_by_name('fazeel')
# remove_emp(emp_1)
# c.execute("SELECT * FROM employee")
# print(c.fetchall())
#
# conn.close()

# ---------------------

# c.execute("DROP TABLE employee")

# c.execute("INSERT INTO employee VALUES (1, 'abrar', 'hassan', 50000)")
# conn.commit()
# c.execute("INSERT INTO employee VALUES (2, 'faheem', 'hassan', 70000)")
# conn.commit()

# c.execute("INSERT INTO employee VALUES ('faheem', 'hassan', 70000)")
# conn.commit()

# c.execute(f"INSERT INTO employee VALUES ('{emp_1.first}', '{emp_1.last}', '{emp_1.pay}')")
# conn.commit()
# c.execute("INSERT INTO employee VALUES (?, ?, ?)", (emp_2.first, emp_2.last, emp_2.pay))
# conn.commit()
# c.execute("INSERT INTO employee VALUES (:first, :last, :pay)",
#   {'first': emp_3.first, 'last': emp_3.last, 'pay': emp_3.pay})
# conn.commit()

# c.execute("SELECT * FROM employee")
# c.execute("SELECT * FROM employee WHERE last=:last", {'last': 'abbas'})
# print(c.fetchall())
# conn.commit()
# conn.close()