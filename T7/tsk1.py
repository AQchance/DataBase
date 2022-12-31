import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

#添加账户
user = input("请输入教师账号：")
password = input("请输入密码：")

# 插入数据
cursor.execute("INSERT INTO Users (username, passwd) VALUES (?, ?)", (user, password))
conn.commit()

# 关闭连接
cursor.close()
conn.close()
