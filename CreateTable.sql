create table Lab
(
    Lno char(10) PRIMARY KEY,   /*实验室的编号*/
    Lname char(20) unique       /*实验室的名字*/
);

create table Labmessage         /*实验室的名字这里认为也是唯一的，*/
(
    Lname char(20) PRIMARY KEY, /*实验室名字*/
    Lcapacity int not null,     /*实验室的容量*/
    Luse char(30),              /*实验室的用途*/
    Lpicture char(30)           /*实验室的图片*/
)

create table Teacher
(
    Tno char(10) PRIMARY KEY,      /*教师的ID*/
    Tphone char(20)                 /*教师的手机号码*/
);                                  /*ID和手机号都具有唯一性，因此为避免传递性，使其成为三范式，分成两个表*/

create table Teachermessage
(   
    Tphone char(20) PRIMARY key,    /*教师的电话号码*/
    Tname char(20),                 /*教师的姓名，可能有重名，因此不会存在传递性*/
    Tbelong char(10),               /*教师所归属的实验室*/
    FOREIGN KEY(Tbelong) REFERENCES Lab(Lno)    /*Tbelong显然是外码*/
);

create table ReserveTable           /*预约表*/
(
    ReserveLabNo char(10),          /*预约的实验室的编号*/
    ReservePersonName char(20),     /*预约人的姓名*/
    ReservePersonPhone char(20),    /*由于预约人的姓名可能会有重名导致无法确认预约的唯一性，需要加上电话号码*/
    ReserveTime char(30),           /*预约的时间*/
    PRIMARY KEY (ReserveLabNo,ReservePersonPhone,ReserveTime),   /*这三个才可以唯一确定一次预约，故主码为这三个*/
    FOREIGN KEY(ReserveLabNo) REFERENCES Lab(Lno),      /*实验室编号是外码*/
    FOREIGN KEY(ReservePersonPhone) REFERENCES Teachermessage(Tphone)   /*使用者电话也是外码，且可以唯一确定预约者*/
);

create table Device                             /*设备信息*/
(
    Dno char(10) PRIMARY KEY,                   /*设备的编号*/
    Dfunc char(30),                             /*设备的功能*/
    Dbelong char(10),                           /*设备所归属的实验室*/
    FOREIGN KEY(Dbelong) REFERENCES Lab(Lno)    /*设备所归属的实验室是外码*/ 
);

go
