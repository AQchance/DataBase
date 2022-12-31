import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 按照年份删除实验室的预约信息
time = input("请输入年份：")
time += '%'
# 删除信息
cursor.execute("DELETE FROM ReserveTable WHERE ReserveTime like ?", (time,))
conn.commit()
print("删除成功！")

# 关闭连接
cursor.close()
conn.close()
