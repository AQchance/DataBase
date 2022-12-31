import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 插入实验室设备的信息
dno = input("请输入设备编号：")
dfunc = input("请输入设备功能：")
dbelong = input("请输入设备所属实验室的号码：")

# 插入数据
cursor.execute("INSERT INTO Device (Dno, Dfunc, Dbelong) VALUES (?, ?, ?)", (dno, dfunc, dbelong))
conn.commit()

# 关闭连接
cursor.close()
conn.close()
