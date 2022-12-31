import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=test;UID=user;PWD=password")
cursor = conn.cursor()

#修改实验设备的信息
dno = input("请输入要修改的设备的编号：")
dbelong = input("请输入要修改的实验室编号内容：")

# 修改表
cursor.execute("UPDATE Device SET Dbelong=? WHERE id=?", (dbelong, dno))

# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
