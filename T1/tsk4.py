import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

#插入实验室预约表的信息
reservelabno = input("请输入预约实验室的编号")
reservepersonname = input("请输入预约教师姓名：")
reservepersonphone = input("请输入预约教师的电话号码：")
reservetime = input("请输入预约时间：")

# 插入数据
cursor.execute("INSERT INTO ReserveTable (ReserveLabNo, ReservePersonName, ReservePersonPhone, "
               "ReserveTime)  VALUES (?, ?, ?, ?)", (reservelabno, reservepersonname, reservepersonphone, reservetime))
conn.commit()

# 关闭连接
cursor.close()
conn.close()
