import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 查询教师信息
tno = input("请输入要查询的教师的编号：")

# 执行查询
cursor.execute("SELECT * FROM Teacher, Teachermessage where Teacher.Tphone=Teachermessage.Tphone and Teacher.Tno=?",(tno,))

# 获取所有查询结果
results = cursor.fetchall()

# 处理结果
for row in results:
  print(row)

# 关闭连接
cursor.close()
conn.close()
