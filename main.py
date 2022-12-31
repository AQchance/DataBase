#主界面
import pyodbc
import pyodbc
from tkinter import *
import T1
import T2
import T3
import T4
import T5
import T6

index.login()

print("****欢迎进入场地预约管理系统****")
while 1:
    print("选择要进行的操作：")
    print("输入1进行信息录入，输入2进行信息查询，输入3进行信息修改，输入4进行信息删除，输入5进行信息统计，输入6进行密码维护，输入7退出\n")
    a = input("请输入指令:")
    if a==1:
        print("**信息录入**")
        print("输入a教师信息录入，输入b实验室信息录入，输入c设备信息录入，输入d预约信息录入\n")
        T=input("请输入指令")
        if T=='a':
            T1.tsk1()
        elif T=='b':
            T1.tsk2()
        elif T=='c':
            T1.tsk3()
        elif T=='d':
            T1.tsk4()
        else:
            print("输入错误")
    elif a==2:
        print("**信息查询**")
        print("输入a教师信息查询，输入b实验室信息查询，输入c设备信息查询，输入d教师预约信息查询，输入f日期查询预约情况，输入g实验室编号查询预约情况\n")
        T=input("请输入指令")
        if T=='a':
            T2.tsk1()
        elif T=='b':
            T2.tsk2()
        elif T=='c':
            T2.tsk3()
        elif T=='d':
            T2.tsk4()
        elif T=='f':
            T2.tsk5()
        elif T=='g':
            T2.tsk6()
        else:
            print("输入错误")
    elif a==3:
        print("**信息修改**")
        print("输入a设备信息修改，输入b实验室信息修改，输入c教师信息修改\n")
        T=input("请输入指令")
        if T=='a':
            T3.tsk1()
        elif T=='b':
            T3.tsk2()
        elif T=='c':
            T3.tsk3()
        else:
            print("输入错误")
    elif a==4:
        print("**信息删除**")
        print("输入a设备信息删除，输入b实验室信息删除，输入c教师信息删除，输入d教师预约信息删除，输入f实验室预约情况删除\n")
        T=input("请输入指令")
        if T=='a':
            T4.tsk1()
        elif T=='b':
            T4.tsk2()
        elif T=='c':
            T4.tsk3()
        elif T=='d':
            T4.tsk4()
        elif T=='f':
            T4.tsk5()
        else:
            print("输入错误")

    elif a == 5:
        print("**信息统计**")
        T5.tsk1()
    elif a == 6:
        print("**密码维护**")
        print("输入a添加账户，输入b修改密码")
        T=input("请输入指令")
        if T=='a':
            T6.tsk1()
        elif T=='b':
            T6.tsk2()
        else:
            print("输入错误")
    elif a == 7:
        print("**退出**")
        break
    else:
        print("不要输入无关指令，请重新输入")

