# Employee Management System, By Ojas Deshpande
# Github:https://github.com/ojasd07/
# Repository Link (Github):https://github.com/OjasD07/employee-management-system-python-mysql


# This is a simple Employee Management System that allows the user to Add, Display, Update, Search and Remove Employee's Record.
# The Employee's Record is stored in a MySQL Database. The user can perform all the operations on the Employee's Record using this system.
# Note: The user needs to have MySQL installed and a database named "Employee_Data" with a table named "Employee" to run this system. The user also needs to update the MySQL connection details in the code (host, user, password) before running the system.
# The code is written in Python and uses the mysql.connector library to connect to the MySQL database. The code is structured in a way that each operation (Add, Display, Update, Search, Remove) is implemented as a separate function. The menu function is used to display the menu and to call the appropriate function based on the user's choice.
# The code is simple and easy to understand, and it can be used as a basic template for an Employee Management System. The user can further enhance the system by adding more features such as sorting, filtering, and generating reports based on the Employee's Record.
# The user can also add error handling to the code to handle exceptions that may occur during database operations. Overall, this Employee Management System provides a basic framework for managing Employee's Record in a MySQL database using Python.

# The Employee's Record consists of the following details:
# 1. Employee ID (EID)
# 2. Employee Joining Date (EJoining_Date)
# 3. Employee Name (EName)
# 4. Employee Phone Number (EPhone_Number)
# 5. Employee Date of Birth (EDOB)
# 6. Employee Address (EAddress)
# 7. Employee Post (EPost)
# 8. Employee Salary (ESalary)

# Constraints on Employee's Record:
# 1. Employee ID should be unique and should not be empty.
# 2. Employee Joining Date should be in the format of YYYYMMDD and should not be empty.
# 3. Employee Name should not be empty and should not exceed 50 characters.
# 4. Employee Phone Number should be 10 digits long,unique and should not be empty.
# 5. Employee Date of Birth should be in the format of YYYYMMDD and should not be empty.
# 6. Employee Address should not be empty and should not exceed 200 characters.
# 7. Employee Post should not be empty and should not exceed 20 characters.
# 8. Employee Salary should not be empty and should be a positive integer.

# The user can perform the following operations on the Employee's Record:
# 1. Add Employee: The user can add a new Employee's Record to the database. The user will be prompted to enter the Employee's details. The system will check if the Employee ID already exists in the database. If it does, the system will display a message and will not add the Employee's Record. If it does not, the system will add the Employee's Record to the database and will display a success message.
# 2. Display Employee: The user can display all the Employee's Record from the database. The system will display all the Employee's Record in a formatted manner. If there are no Employee's Record in the database, the system will display a message.
# 3. Update Employee: The user can update the Employee's Record in the database. The user will be prompted to enter the Employee ID. The system will check if the Employee ID exists in the database. If it does, the user will be prompted to enter the new Employee's Phone Number and Address. The system will update the Employee's Record in the database and will display a success message. If it does not, the system will display a message.
# 4. Search Employee: The user can search for a Employee's Record in the database. The user will be prompted to enter the Employee ID. The system will check if the Employee ID exists in the database. If it does, the system will display the Employee's Record in a formatted manner. If it does not, the system will display a message.
# 5. Remove Employee: The user can remove a Employee's Record from the database. The user will be prompted to enter the Employee ID. The system will check if the Employee ID exists in the database. If it does, the system will remove the Employee's Record from the database and will display a success message. If it does not, the system will display a message.
# The user can exit the system by entering 6 in the menu.



import mysql.connector
connection = mysql.connector.connect(host="localhost", user="root",password="Your_Password", database="Employee_Data")

# Function to Add Employee
def Add_Employee():
    print("\nAdd Employee's Record-->")
    EID = input ("\nEnter Employee's ID:")
    # Checking if Employee Id is existing
    if(check_employee(EID) == False) :
        EJoining_Date = int(input("Enter Employee's Date of Joining [YYYYMMDD]:"))
        if len(str(EJoining_Date)) == 8:
            EName = input("Enter Employee's Name:")
            if len(EName) <= 50:
                EPhone_Number = input("Enter Employee's Phone Number:")
                if len(EPhone_Number) == 10:
                    if (check_employee_EPhone_Number(EPhone_Number) == False) :
                        EDOB = int(input("Enter Employee's Date of Birth [YYYYMMDD]:"))
                        if len(str(EDOB)) == 8:
                            EAddress = input("Enter Employee's Address:" )
                            if len(EAddress) <= 200:
                                EPost = input("Enter Employee's Post:")
                                if len(EPost) <= 20:
                                    ESalary = input("Enter Employee's Salary:")
                                    data = (EID, EJoining_Date, EName, EPhone_Number, EDOB, EAddress, EPost, ESalary)
                                    # Inserting Employee Details into the Employee_Data (Employee) Table
                                    sql = 'insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s)'
                                    cursor = connection.cursor()
                                    cursor.execute(sql, data)
                                    connection.commit()
                                    print("\nSuccessfully Added Employee's Record.")
                                    press = input("\nPress Any Key To Continue.")
                                    menu()
                                else:
                                    print("\nPost is too Long!")
                                    press = input ("\nPress Any Key To Continue.")
                                    menu()
                            else:
                                print("\nAddress is too Long!")
                                press = input ("\nPress Any Key To Continue.")
                                menu()
                        else:
                            print("\nDate of Birth is Invalid!")
                            press = input ("\nPress Any Key To Continue.")
                            menu()
                    else:
                        print("\nPhone Number Already Exists!")
                        press = input ("\nPress Any Key To Continue.")
                        menu()
                else:
                    print("\nPhone Number is Invalid!")
                    press = input ("\nPress Any Key To Continue.")
                    menu()
            else:
                print("\nName is too long!")
                press = input ("\nPress Any Key To Continue.")
                menu()
        else:
            print("\nDate of Joining is invalid!")
            press = input ("\nPress Any Key To Continue.")
            menu()
    else:
        print("\nEmployee ID Already Exists!")
        press = input ("\nPress Any Key To Continue.")
        menu()

# Function to Check if Employee with given EPhone_Number exists
def check_employee_EPhone_Number(employee_phone_no):
    sql = 'select * from Employee where EPhone_Number = %s'
    cursor = connection.cursor(buffered=True)
    data = (employee_phone_no,)
    cursor.execute(sql, data)
    rows = cursor.rowcount
    if rows == 1:
        return True
    else:
        return False

# Function to Check if Employee with given EID exists
def check_employee(employee_id):
    sql = 'select * from Employee where EID = %s'
    cursor = connection.cursor(buffered=True)
    data = (employee_id,)
    cursor.execute(sql, data)
    rows = cursor.rowcount
    if rows == 1:
        return True
    else:
        return False

# Function to Display Employee
def Display_Employee():
    print("\nDisplay Employee's Record--> ")
    # Query to select all rows from Employee_Data (Employee) Table
    sql = 'select * from Employee'
    cursor = connection.cursor()
    cursor.execute(sql)
    # Fetching all details of all the Employees
    details = cursor.fetchall ( )
    rows = cursor.rowcount
    if rows == 0:
        print("\nEmployee Record does not Exist!")
        press = input("\nPress Any Key To Continue.")
        menu()
    else :
        for i in details:
            print("\nEmployee's Id: ", i[0])
            print("Employee's Joining Date: ", i[1])
            print("Employee's Name: ", i[2])
            print("Employee's Phone Number: ", i[3])
            print("Employee's Date of Birth: ", i[4])
            print("Employee's Address: ", i[5])
            print("Employee's Post: ", i[6])
            print("Employee's Salary: ", i[7])
        else:
            press = input("\nPress Any Key To Continue.")
            menu()
            
# Function to Update Employee
def Update_Employee():
    print("\nUpdate Employee's Record-->")
    EID = input("\nEnter Employee's ID: ")
    # Checking If Employee Id exists
    if (check_employee(EID) == True):
        EPhone_Number = input("Enter Employee's Phone Number: ")
        if len(EPhone_Number) == 10:
            if (check_employee_EPhone_Number(EPhone_Number) == False) :
                EAddress = input("Enter Employee's Address: ")
                if len(EAddress) <= 200:
                    # Updating Employee details in Employee_Data (Employee) Table
                    sql = 'UPDATE Employee SET EPhone_Number = %s, EAddress = %s WHERE EID = %s'
                    data = (EPhone_Number, EAddress, EID)
                    cursor = connection.cursor()
                    cursor.execute(sql, data)
                    connection.commit()
                    print("\nUpdated Employee's Record")
                    press = input("\nPress Any Key To Continue.")
                    menu()
                else:
                    print("\nAddress is too Long!")
                    press = input ("\nPress Any Key To Continue.")
                    menu()
            else:
                print("\nPhone Number Already Exists!")
                press = input ("\nPress Any Key To Continue.")
                menu()
        else:
            print("\nPhone Number is Invalid!")
            press = input ("\nPress Any Key To Continue.")
            menu()
    else :
        print("\nEmployee Record does not exist!")
        press = input("\nPress Any Key To Continue.")
        menu()

# Function to Remove_Employee
def Remove_Employee():
    print("\nRemove Employee's Record-->")
    EID = input("\nEnter Employee's ID:")
    # Checking If Employee Id is exists
    if (check_employee(EID) == False):
        print("\nEmployee's Record does not exist!")
        press = input("\nPress Any Key To Continue.")
        menu()
    else:
        # Query to delete Employee from Employee table
        sql = 'delete from Employee where EID = %s'
        data = (EID,)# Converting it into tuple.
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        print("\nEmployee Removed!")
        press = input("\nPress Any key To Continue.")
        menu()

# Function to Search Employee
def Search_Employee():
    print("\nSearch Employee's Record-->")
    EID = input("\nEnter Employee ID: ")
    # Checking If Employee Id exists
    if (check_employee(EID) == True):
    # Query to search Employee from Employee table
        sql = 'select * from Employee where EID = %s'
        data = (EID,)#Converting it into tuple.
        cursor = connection.cursor()
        cursor.execute(sql, data)
        # Fetching all details of all the employee
        details = cursor.fetchall()
        for i in details:
            print("\nEmployee's Id: ", i[0])
            print("Employee's Joining Date: ", i[1])
            print("Employee's Name: ", i[2])
            print("Employee's Phone Number: ", i[3])
            print("Employee's Date of Birth: ", i[4])
            print("Employee's Address: ", i[5])
            print("Employee's Post: ", i[6])
            print("Employee's Salary: ", i[7])
            press = input("\nPress Any key To Continue.")
            menu()
    else:
        print("\nEmployee Record does not Exist!")
        press = input("\nPress Any Key To Continue.")
        menu()


# Menu function to display menu
def menu():
    print("-------------------------------------")
    print("Employee Management System")
    print("-------------------------------------")
    print("    1. Add Employee")
    print("    2. Display Employee's Record")
    print("    3. Update Employee's Record")
    print("    4. Remove Employee's Record")
    print("    5. Search Employee's Record")
    print("    6. Exit")
    print("-------------------------------------")
    print("Choice Options: [1/2/3/4/5/6]:")
    print("-------------------------------------")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Employee()
    elif ch == 2:
        Display_Employee()
    elif ch == 3:
        Update_Employee()
    elif ch == 4:
        Remove_Employee()
    elif ch == 5:
        Search_Employee()
    elif ch == 6:
        print("THANK YOU!")
        exit(0)
    else:
        print("\nInvalid Choice!")
        press = input("\nPress Any key To Continue.")
        menu()

menu()
