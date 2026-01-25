# Employee Management System, By Ojas Deshpande

from os import system
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root",password="12345678", database="Employee_Data")

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
                                    c = con.cursor()
                                    c.execute(sql, data)
                                    con.commit()
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
    c = con.cursor(buffered=True)
    data = (employee_phone_no,)
    c.execute(sql, data)
    a = c.rowcount
    if a == 1:
        return True
    else:
        return False

# Function to Check if Employee with given EID exists
def check_employee(employee_id):
    sql = 'select * from Employee where EID = %s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    a = c.rowcount
    if a == 1:
        return True
    else:
        return False

# Function to Display Employee
def Display_Employee():
    print("\nDisplay Employee's Record--> ")
    # Query to select all rows from Employee_Data (Employee) Table
    sql = 'select * from Employee'
    c = con.cursor()
    c.execute(sql)
    # Fetching all details of all the Employees
    r = c.fetchall ( )
    a = c. rowcount
    if a == 0:
        print("\nEmployee Record does not Exist!")
        press = input("\nPress Any Key To Continue.")
        menu()
    else :
        for i in r:
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
                    c = con.cursor()
                    c.execute(sql, data)
                    con.commit()
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
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
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
        c = con.cursor()
        c.execute(sql, data)
        # Fetching all details of all the employee
        r = c.fetchall()
        for i in r:
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
