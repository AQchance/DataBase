import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=test;UID=user;PWD=password")
cursor = conn.cursor()

# 按照实验室号删除实验室相关信息
lno = input("请输入实验室编号：")

# 执行查询
cursor.execute("SELECT * FROM Lab WHERE Lno=?", (lno,))
row = cursor.fetchone()
lname=row[1]

# 删除信息
cursor.execute("DELETE FROM Lab WHERE Lno=?", (lno,))
conn.commit()

cursor.execute("DELETE FROM Labmessage WHERE Lname=?", (lname,))
# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
