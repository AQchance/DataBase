import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

username=input()
password=input()
cursor.execute("SELECT * FROM Users where username=? and passwd=?",(username,password))
results = cursor.fetchall()
ret=0
for row in results:
    ret+=1
print(ret)
cursor.close()
conn.close()