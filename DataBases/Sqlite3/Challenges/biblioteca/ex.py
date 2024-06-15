import sqlite3
import datetime

# Função para criar o banco de dados e suas tabelas
def criar_banco_dados():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    # Criação das tabelas
    cursor.execute('''CREATE TABLE IF NOT EXISTS Autores (
                        id INTEGER PRIMARY KEY,
                        nome TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Editoras (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        localizacao TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT,
                        ano_publicacao INTEGER,
                        id_autor INTEGER,
                        id_editora INTEGER,
                        FOREIGN KEY (id_autor) REFERENCES Autores(id),
                        FOREIGN KEY (id_editora) REFERENCES Editoras(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        email TEXT,
                        endereco TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Emprestimos (
                        id INTEGER PRIMARY KEY,
                        id_usuario INTEGER,
                        id_livro INTEGER,
                        data_emprestimo DATE,
                        data_devolucao DATE,
                        FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
                        FOREIGN KEY (id_livro) REFERENCES Livros(id)
                    )''')

    conexao.commit()
    conexao.close()

# Função para inserir novos autores
def inserir_autor(nome):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO Autores (nome) VALUES (?)", (nome,))
        conexao.commit()
        print("Autor inserido com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: O autor já existe.")

    conexao.close()

# Função para inserir nova editora
def inserir_editora(nome, localizacao):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO Editoras (nome, localizacao) VALUES (?, ?)", (nome, localizacao))
        conexao.commit()
        print("Editora inserida com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: A editora já existe.")

    conexao.close()

# Função para inserir novo livro
def inserir_livro(titulo, ano_publicacao, id_autor, id_editora):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO Livros (titulo, ano_publicacao, id_autor, id_editora) VALUES (?, ?, ?, ?)", (titulo, ano_publicacao, id_autor, id_editora))
        conexao.commit()
        print("Livro inserido com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: O livro já existe ou o autor/editora não foi encontrado.")

    conexao.close()

# Função para inserir novo usuário
def inserir_usuario(nome, email, endereco):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO Usuarios (nome, email, endereco) VALUES (?, ?, ?)", (nome, email, endereco))
        conexao.commit()
        print("Usuário inserido com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: O usuário já existe.")

    conexao.close()

# Função para realizar um empréstimo
def emprestar_livro(id_usuario, id_livro):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    # Verifica se o livro está disponível
    cursor.execute("SELECT * FROM Emprestimos WHERE id_livro = ?", (id_livro,))
    emprestimos = cursor.fetchall()
    if emprestimos:
        print("Erro: O livro já está emprestado.")
        return

    # Obtém a data atual
    data_emprestimo = datetime.date.today()

    # Calcula a data de devolução (7 dias a partir da data de empréstimo)
    data_devolucao = data_emprestimo + datetime.timedelta(days=7)

    try:
        cursor.execute("INSERT INTO Emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", (id_usuario, id_livro, data_emprestimo, data_devolucao))
        conexao.commit()
        print("Livro emprestado com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: O usuário ou livro não foi encontrado.")

    conexao.close()

# Função para excluir um usuário e seus empréstimos associados
def excluir_usuario(id_usuario):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM Usuarios WHERE id = ?", (id_usuario,))
        conexao.commit()
        print("Usuário excluído com sucesso.")

        cursor.execute("DELETE FROM Emprestimos WHERE id_usuario = ?", (id_usuario,))
        conexao.commit()
        print("Empréstimos associados ao usuário excluídos.")
    except sqlite3.IntegrityError:
        print("Erro: O usuário não foi encontrado.")

    conexao.close()

# Função para realizar backup do banco de dados
def fazer_backup():
    import shutil
    shutil.copy2('biblioteca.db', 'backup_biblioteca.db')
    print("Backup realizado com sucesso.")

# Função para restaurar o banco de dados a partir do backup
def restaurar_backup():
    import os
    if os.path.exists('backup_biblioteca.db'):
        os.replace('backup_biblioteca.db', 'biblioteca.db')
        print("Backup restaurado com sucesso.")
    else:
        print("Erro: Backup não encontrado.")

# Função para criar índices nas colunas relevantes
def criar_indices():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    # Índice para a coluna 'nome' na tabela 'Usuarios'
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_nome_usuario ON Usuarios (nome)")

    # Índice para a coluna 'titulo' na tabela 'Livros'
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_titulo_livro ON Livros (titulo)")

    conexao.commit()
    conexao.close()
    print("Índices criados com sucesso.")

if __name__ == "__main__":
    criar_banco_dados()
    
    # Inserção de dados
    inserir_autor("João Silva")
    inserir_editora("Editora A", "São Paulo")
    inserir_livro("Livro X", 2020, 1, 1)
    inserir_usuario("Maria Oliveira", "maria@example.com", "Rua ABC, 123")
    
    # Consulta de dados
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Livros WHERE id_autor = 1")
    livros_autor = cursor.fetchall()
    print("Livros do autor:")
    print(livros_autor)
    
    cursor.execute("SELECT * FROM Emprestimos WHERE id_usuario = 1")
    emprestimos_usuario = cursor.fetchall()
    print("Empréstimos do usuário:")
    print(emprestimos_usuario)
    
    # Atualização de dados
    # Vamos supor que queremos atualizar o título do livro com ID 1
    cursor.execute("UPDATE Livros SET titulo = 'Livro Y' WHERE id = 1")
    conexao.commit()
    print("Título do livro atualizado com sucesso.")
    
    # Exclusão de dados
    excluir_usuario(1)
    
    # Transações
    emprestar_livro(2, 1)
    
    # Backup e Restauração
    fazer_backup()
    restaurar_backup()
    
    # Indexação e Otimização
    criar_indices()
