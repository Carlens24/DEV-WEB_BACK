# inserting all de data correctly on their columns
insert into employees values
(default, 'carlens', 'oslin', '700.00', '23-12-14', '41-997809090'),
(default, 'Schneidine', 'oslin', '600.00', '22-06-12', '41-997809090');

# inserting the data on the column that was especificated
insert into employees (id, fstname, lstname, payment, hire_date) values
(default, 'João', 'Silva', 300.50, '2023-01-15'),
(default, 'Maria', 'Santos', 350.75, '2022-05-20'),
(default, 'Carlos', 'Oliveira', 400.00, '2023-09-10'),
(default, 'Ana', 'Souza', 300.25, '2024-02-03'),
(default, 'Pedro', 'Ferreira', 320.00, '2023-11-18'),
(default, 'Juliana', 'Almeida', 370.50, '2022-08-25'),
(default, 'Ricardo', 'Rodrigues', 420.75, '2023-04-12'),
(default, 'Amanda', 'Gomes', 310.00, '2024-01-07'),
(default, 'Fernanda', 'Martins', 390.25, '2022-12-30'),
(default, 'Lucas', 'Ramos', 330.80, '2023-06-29');
 

select * from employees;
