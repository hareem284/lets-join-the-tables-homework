
import sqlite3
#importing pandas
import pandas as pd
#connecting with database
conndb=sqlite3.connect("basketball.sqlite")
print("connection is eastablished,hip hip hooray hipp hip hooray hip hip hooray!!!!!!!!!!!!!!!!")
#reading data base file
reading=pd.read_sql("SELECT * FROM Player;",conndb)
print(reading.info())
print(reading.head(10))
#checking salaries 
checkingsalary=pd.read_sql("SELECT * FROM Player_Salary;",conndb)
print(checkingsalary.info())
