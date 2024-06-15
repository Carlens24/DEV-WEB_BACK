alter table product
modify price decimal(4, 2) not null;

# testing the null

insert into product values (104, 'Cookie', null);

select * from product;