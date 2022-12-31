import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 通过日期查询预约记录
time = input("请输入日期（年或年月或年月日，用点号分隔）：")
time += '%'

# 执行查询
cursor.execute("SELECT * FROM ReserveTable where ReserveTime like ?",(time,))

# 获取所有查询结果
results = cursor.fetchall()
# 处理结果
print("实验室编号\t姓名\t电话号\t预约时间")
for row in results:
  print(row)


# 关闭连接
cursor.close()
conn.close()
