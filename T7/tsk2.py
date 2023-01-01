import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

#对教师账户密码的修改
user = input("输入用户名：")
flag=0
while flag!=1:
    password1 = input("输入密码：")
    password2 = input("确认密码：")
    if password1 == password2:
        flag=1
    else:
        print("两次密码输入不匹配，请重新输入")

# 修改表
cursor.execute("UPDATE Users SET passwd=? WHERE username=?", (user,password1))
print("修改成功！")
# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
