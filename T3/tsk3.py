import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=test;UID=user;PWD=password")
cursor = conn.cursor()

#修改教师的相关信息
tno = input("请输入要修改的教师的ID号码：")
tbelong = input("请输入要修改的教师的所属实验室：")

# 执行查询
cursor.execute("SELECT * FROM Teacher WHERE Tno=?", (tno,))
row = cursor.fetchone()
tphone=row[1]
# 修改表
cursor.execute("UPDATE Teachermessage SET Tbelong=? WHERE Tphone=?", (tbelong, tphone))

# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
