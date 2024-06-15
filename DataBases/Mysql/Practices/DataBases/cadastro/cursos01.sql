create table cursos (
nome varchar(30) not null unique,
descricao text,
carga int unsigned,
totaulas int unsigned,
ano year default '2024'
) default charset = utf8;

alter table cursos
add column idcursos INT first;

alter table cursos
add primary key(idcursos);

describe cursos;
