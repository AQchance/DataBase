import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 按照教师编号删除教师相关信息
tno = input("请输入教师编号：")

# 执行查询
cursor.execute("SELECT * FROM Teacher WHERE Tno=?", (tno,))
row = cursor.fetchone()
tphone=row[1]

# 删除信息
cursor.execute("DELETE FROM Teacher WHERE Tno=?", (tno,))
conn.commit()

cursor.execute("DELETE FROM Teachermessage WHERE Tphone=?", (tphone,))
# 提交更改
conn.commit()
print("删除成功！")
# 关闭连接
cursor.close()
conn.close()
