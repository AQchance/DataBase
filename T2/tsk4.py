import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 查询教师的预约记录
tname = input("请输入要查询的教师的姓名：")

# 执行查询
cursor.execute("SELECT * FROM ReserveTable where ReservePersonName=?",(tname,))

# 获取所有查询结果
results = cursor.fetchall()

# 处理结果
print("实验室编号\t姓名\t电话号\t预约时间")
for row in results:
  print(row)


# 关闭连接
cursor.close()
conn.close()
