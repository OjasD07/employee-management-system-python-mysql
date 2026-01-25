# Employee Management System

A console-based Employee Management System built using **Python** and **MySQL**.

This project was developed as part of the **Class XII Computer Science** curriculum and implements basic backend and database functionality.

## Features
- Add, display, update, search, and delete employee records
- Menu-driven console interface
- MySQL database with primary key constraints

## Tech Stack
- Python
- MySQL

## How to Run
1. Ensure MySQL is installed and running
2. Create the database and table as shown in the project code
______________________________________________________________
   mysql> create database Employee_Data;
   mysql> use Employee_Data;
   mysql> Create table Employee(
    -> EID INT NOT NULL,
    -> EJoining_Date DATE NOT NULL,
    -> EName VARCHAR(50) NOT NULL,
    -> EPhone_Number BIGINT NOT NULL,
    -> EDOB DATE NOT NULL,
    -> EAddress VARCHAR(200) NOT NULL,
    -> EPost VARCHAR(20) NOT NULL,
    -> ESalary INT NOT NULL,
    -> PRIMARY KEY (EID));
______________________________________________________________

3. Install dependency:
   ```bash
   pip install mysql-connector-python
4. Run the Python file
