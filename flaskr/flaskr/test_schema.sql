drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);
insert into users values(1, 'admin', 'default');
insert into users values(2, 'test', 'Hema7067');

