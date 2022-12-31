import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

#插入实验室信息
lno = input("请输入实验室的编号：")
lname = input("请输入实验室的名字：")
lcapacity = input("请输入实验室的容量：")
luse = input("请输入实验室的用途：")
lpicture = input("请输入实验室的图片：")

# 插入数据
cursor.execute("INSERT INTO Lab (Lno, Lname) VALUES (?, ?)", (lno, lname))
conn.commit()

cursor.execute("INSERT INTO Labmessage (Lname, Lcapacity, Luse, Lpicture) VALUES (?, ?, ?, ?)",
               (lname, lcapacity, luse, lpicture))
conn.commit()

# 关闭连接
cursor.close()
conn.close()
