# Using the check
# criar padrões pra colunas.
create table employees (
id int auto_increment primary key,
nome varchar(50),
pay decimal (5, 2),
hire date,
constraint chk_h check(pay >= 10.00)
);

alter table employees
add constraint chk check(pay >= 10.00);

select * from employees;

insert into employees values
(default, 'anhe', 10.00, '2024-05-08');

# droping the check
alter table employees
drop check chk_h;