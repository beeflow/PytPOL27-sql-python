create table branch
(
    id   int auto_increment primary key,
    name varchar(10)
);

create table model
(
    id        int auto_increment primary key,
    name      varchar(10),
    branch_id int,

    foreign key (branch_id) references branch (id) on delete cascade on update cascade
);


create table car
(
    id              int auto_increment primary key,
    register_number varchar(10),
    color           varchar(10),
    model_id        int,

    foreign key (model_id) references model (id) on delete cascade on update cascade
);

insert into model(name, branch_id)
values ("A4", (select id from branch where name = 'Audi'))