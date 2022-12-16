create table Lab
(
    Lno char(10) PRIMARY KEY,
    Lname char(20) unique,
    Lcapacity int not null,
    Luse char(30),
    Lpicture char(30)
)

create table Teacher
(
    Tno char(10) PRIMARY KEY,
    Tname char(20) unique,
    Tphone char(20) unique,
    Tbelong char(10),
    FOREIGN KEY(Tbelong) REFERENCES Lab(Lno)
);

create table ReserveTable
(
    ReserveLabNo char(10),
    ReservePersonName char(20),
    ReserveTime char(30),
    PRIMARY KEY (ReserveLabNo,ReservePersonName,ReserveTime),
    FOREIGN KEY(ReserveLabNo) REFERENCES Lab(Lno),
    FOREIGN KEY(ReservePersonName) REFERENCES Teacher(Tname)
);

create table Device
(
    Dno char(10) PRIMARY KEY,
    Dfunc char(30),
    Dbelong char(10),
    FOREIGN KEY(Dbelong) REFERENCES Lab(Lno)
);

go
