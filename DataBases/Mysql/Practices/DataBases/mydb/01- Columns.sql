# Database creation
create database if not exists myDB; 

# The table an columns creations
create table if not exists empleyees(
id int,
fstname varchar(50),
lstname varchar(50),
payment decimal(5, 2),
hire_date date
);

# rename table
rename table workers to employees;
 
 # rename column
alter table employees
rename column frstname to fstname;
 
 # add new column
alter table employees
add phone varchar(20);

alter table employees
add email varchar(10);
 
 # altering the number of characters of the email
 alter table employees
 modify column email varchar(100);
 
 alter table employees
 modify fstname varchar(50);
 
 alter table employees
 modify lstname varchar(50);
 
alter table employees
modify column id int auto_increment primary key;


 # moving the email position to after the last name column
alter table employees
modify email varchar(100)
after lstname
; # Or first

# droping table
alter table employees
drop column email;
  
# The results
select * from employees;
desc employees;


