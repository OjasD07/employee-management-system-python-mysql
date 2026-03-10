# Employee Management System (Python + MySQL)

A console-based CRUD application to manage employee records using Python and MySQL.
This project was developed as part of the **Class XII Computer Science** curriculum and implements basic backend and database functionality.
## Features
- Add new employees
- Display all employee records
- Search employee by ID
- Update employee phone number and address
- Delete employee records
- Input checks for basic field length and duplicate IDs/phone numbers

## Tech Stack
- Python
- MySQL
- `mysql-connector-python`

## Project Files
- `Employee Management System.py`: Main Python application
- `schema.sql`: Database and table creation script

## Database Schema
The app uses:
- Database: `Employee_Data`
- Table: `Employee`
- Primary key: `EID`

Columns:
- `EID` (INT)
- `EJoining_Date` (DATE)
- `EName` (VARCHAR(50))
- `EPhone_Number` (BIGINT)
- `EDOB` (DATE)
- `EAddress` (VARCHAR(200))
- `EPost` (VARCHAR(20))
- `ESalary` (INT)

## Prerequisites
- Python 3.x
- MySQL Server
- Python package: `mysql-connector-python`

## Setup and Run
1. Install Python dependency:
```bash
pip install mysql-connector-python
```

2. Create the database/table:
```bash
mysql -u root -p < schema.sql
```

3. Open `Employee Management System.py` and update MySQL credentials in:
```python
mysql.connector.connect(host="localhost", user="root", password="Your_Password", database="Employee_Data")
```

4. Run the application:
```bash
python "Employee Management System.py"
```

## Menu Options
1. Add Employee  
2. Display Employee Records  
3. Update Employee Record  
4. Remove Employee Record  
5. Search Employee Record  
6. Exit

## Notes
- Date inputs are prompted as `YYYYMMDD`.
- This is a console project in its original academic style.

## Author
Ojas Deshpande [contact.ojasdeshpande@gmail.com]
