import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

#修改实验室的相关信息
lno = input("请输入要修改的实验室的编号：")
lname = input("请输入要修改的实验室名字内容：")

# 执行查询
cursor.execute("SELECT * FROM Lab WHERE Lno=?", (lno,))
row = cursor.fetchone()
ln=row[1]
# 修改表
cursor.execute("UPDATE Lab SET Lname=? WHERE Lno=?", (lname, lno))
cursor.execute("UPDATE Labmessage SET Lname=? WHERE Lname=?", (lname, ln))

# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
