import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

time=0

# 执行查询
cursor.execute("SELECT ReserveTime FROM ReserveTable")

# 获取所有查询结果
results = cursor.fetchall()

# 处理结果
for row in results:
  time+=3.5
day=time/24
month=day/30
print("各实验室的总共预约时长为",time,"小时")
print("共计",day,"天",",或者说",month,"个月")
# 关闭连接
cursor.close()
conn.close()
