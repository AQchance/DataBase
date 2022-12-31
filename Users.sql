create table Users
(
    username char(10) PRIMARY KEY,
    passwd char(20),
    FOREIGN KEY(username) REFERENCES Teacher(Tno)
)

go