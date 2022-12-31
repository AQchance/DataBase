import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

#插入教师信息
tno = input("请输入教师的ID号码：")
tname = input("请输入教师姓名：")
tphone = input("请输入教师的电话号码：")
tbelong = input("请输入教师所属实验室号码：")

# 插入数据
cursor.execute("INSERT INTO Teacher (Tno, Tphone) VALUES (?, ?)", (tno, tphone))
conn.commit()

cursor.execute("INSERT INTO Teachermessage (Tphone, Tname, Tbelong) VALUES (?, ?, ?)", (tphone, tname, tbelong))
conn.commit()

# 关闭连接
cursor.close()
conn.close()
