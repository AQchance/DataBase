import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=test;UID=user;PWD=password")
cursor = conn.cursor()

# 按照日期删除某教师某实验室的预约记录
tno = input("请输入教师编号：")
lno = input("请输入实验室编号：")
reservetime = input("请输入要删除的预约记录的日期：")

# 执行查询
cursor.execute("SELECT * FROM Teacher WHERE Tno=?", (tno,))
row = cursor.fetchone()
tphone=row[1]

# 删除信息
cursor.execute("DELETE FROM ReserveTable WHERE ReserveLabNo=? and ReservePersonPhone=? and ReserveTime=?",
               (lno, tphone, reservetime))

# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
