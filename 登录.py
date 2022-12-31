import pyodbc
from tkinter import *
#import page

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-IIB71O59;DATABASE=MYSQL;UID=sa;PWD=duxinpeng0627")
cursor = conn.cursor()

# 设置登录窗口
win = Tk()
win.title('登陆')
win.geometry('300x150')
win.resizable(0, 0)
# 设置账号
Label(text='账号:').place(x=50, y=30)
uname = Entry(win)
uname.place(x=100, y=30)
# 设置密码
Label(text='密码:').place(x=50, y=70)
pwd = Entry(win)
pwd.place(x=100, y=70)

# 登陆
def login():
    username = uname.get()
    password = pwd.get()
    cursor.execute("SELECT * FROM Users where username=? and passwd=?",(username,password))
    results = cursor.fetchall()
    ret=0
    for row in results:
        ret+=1
    cursor.close()
    if ret>0:
      print("登录成功！")
      a=1
    else:
      print("登录失败！")
      a=0
    return a
flog=login()
# 登陆按钮
Button(text='登陆', command=flog).place(x=100, y=110)
if flog==0:
    win.mainloop()
#else:
   # page.show()