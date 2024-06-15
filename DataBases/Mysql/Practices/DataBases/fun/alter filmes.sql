use fun;
desc filmes;

alter table filmes
add column genero varchar(50);

alter table filmes 
drop column genero;

alter table filmes
add column genero varchar(50) after Ano_de_producao;

alter table filmes
add column teste int first;

alter table filmes
modify column genero varchar(50) not null default ' ';

select * from filmes;
