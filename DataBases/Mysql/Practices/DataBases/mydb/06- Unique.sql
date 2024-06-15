create table product (
id int auto_increment primary key not null,
pname varchar(25),
price decimal(4.3)
);

# colocando o unique na coluna pname, caso de esquecimento

alter table product
add constraint
unique(pname);

insert into product values
 (default, 'A', 3.2),
 (default, 'A', 6.5),
 (default, 'C', 9.9),
 (default, 'D', 1.0),
 (default, 'E', 1.7);
 
 # or
 
insert into product values
 (default, 'A', 3.2),
 (default, 'B', 6.5),
 (default, 'C', 9.9),
 (default, 'D', 1.0),
 (default, 'E', 1.7);



select * from product;



