import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 查询实验室的预约记录
lno = input("请输入要查询的实验室的编号：")

# 执行查询
cursor.execute("SELECT * FROM ReserveTable where ReserveLabNo=?",(lno,))

# 获取所有查询结果
results = cursor.fetchall()

# 处理结果
print("实验室编号\t姓名\t电话号\t预约时间")
for row in results:
  print(row)


# 关闭连接
cursor.close()
conn.close()
