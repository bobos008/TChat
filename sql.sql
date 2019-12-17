create database tchat charset="utf8";


create table userinfo(
    id int primary key auto_increment,
    username varchar(100),
    nickname varchar(100),
    email varchar(60),
    password varchar(60)
);

