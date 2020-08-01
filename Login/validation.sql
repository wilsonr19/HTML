create database url;
use url;
create table sign(
id int(10) primary key auto_increment,
name char(30) not null,
email varchar(50) not null,
password varchar(30) not null
);

describe sign;