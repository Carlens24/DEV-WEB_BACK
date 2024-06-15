UPDATE cursos
SET nome = 'HTML5'
WHERE idcursos = '1';

update cursos
set descricao = 'Curso de HTML5'
WHERE idcursos = '1';

update cursos
set nome = 'Java', ano = '2000'
where idcursos = '4';

update cursos
set nome = 'C++', descricao = 'Fundamentos de programação em C++'
where idcursos = '5';

# É uma pena mas não esta dando certo!!!
# Deve ser por causa do update em si mesmo que não quer funcionar
# mais é recomendavel nao usar muiro o update. Quer saber mais? PESQUISE.
update cursos 
set nome = 'Testando', descricao = 'Teste realizado com sucesso!!', carga = '000', totaulas = '000', ano = '000'
where ano = '2000'
limit 3;

# Apagar linhas de vez
delete from cursos
where idcursos= '12';

# Ou 
delete from cursos
where ano = '2000'
limit 1;

# Pra remover todas as linhas de uma vez
truncate table cursos;

SELECT * FROM cursos;
