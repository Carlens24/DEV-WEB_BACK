create table if not exists teste (
id int,
nome varchar(10),
idade int
) charset = utf8;

insert into teste value
('1', 'oslin', '15'),
('2', 'marimota', '22'),
('3', 'caca', '44');

drop table if exists teste;

select * from teste