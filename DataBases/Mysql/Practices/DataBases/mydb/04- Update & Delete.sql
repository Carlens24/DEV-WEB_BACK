update employees
set payment = 10.20,
phone = '41-9987865'
where id = 10;
#Or
update employees
set payment = 10.20,
phone = null
where id = 31;

# all of the rows on a column
update employees
set payment = 10.35;

# delete
delete from employees
where id = 6;

select * from employees

 