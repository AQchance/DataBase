import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 按照设备号删除设备信息
dno = input("请输入设备号：")

# 删除信息
cursor.execute("DELETE FROM Device WHERE Dno=?", (dno,))

# 提交更改
conn.commit()
print("删除成功")

# 关闭连接
cursor.close()
conn.close()
