DESC gafanhotos;

ALTER TABLE pessoas
add column profissão varchar(10) after nome;
# OU
alter table gafanhotos
add column codigo int first; 

alter table gafanhotos 
drop column codigo;

alter table gafanhotos
modify column profissão varchar(20) not null default ' ';
# OU

alter table gafanhotos
change column profissão prof varchar(10);

alter table pessoas
rename to gafanhotos;

SELECT * FROM pessoas