import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 查询设备信息
dno = input("请输入要查询的设备的编号：")

# 执行查询
cursor.execute("SELECT * FROM Device where Dno=?",(dno,))

# 获取所有查询结果
results = cursor.fetchall()

# 处理结果
print("设备编号\t设备功能\t设备所属实验室")
print("分别为：")
for row in results:
  for item in row:
    print(item)


# 关闭连接
cursor.close()
conn.close()
