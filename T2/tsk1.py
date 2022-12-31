import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

#查询实验室信息
tno = input("请输入要查询的实验室的编号：")

# 执行查询
cursor.execute("SELECT * FROM Lab, Labmessage where Lab.Lname=Labmessage.Lname and Lab.Lno=?",(tno,))

# 获取所有查询结果
results = cursor.fetchall()

# 处理结果
for row in results:
  print(row)

# 关闭连接
cursor.close()
conn.close()
