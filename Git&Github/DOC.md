## Resumo
- **Git:** Sistema de controle de versões distribuído para gerenciar o histórico de alterações do código.
- **GitHub:** Plataforma online que hospeda repositórios Git.

## Termos Básicos
- **Directory (Pasta):** Estrutura de armazenamento para organizar arquivos.
- **Terminal ou Linha de Comando (Command Line):** Interface de texto para interagir com o sistema operacional.
- **CLI (Command Line Interface):** Interface de usuário baseada em texto para interação com software.
- **CD (Change Directory):** Comando para mudar o diretório atual no terminal. Exemplo: `cd nome_do_diretorio`
- **Code Editor (Editor de Código):** Software para escrever e editar código. Exemplos: Visual Studio Code, Sublime Text, Atom.
- **Repository (Repositório):** Local de armazenamento do código de um projeto.
- **GitHub:** Plataforma para hospedagem e gerenciamento de repositórios Git.

## Comandos Básicos do Git

- **clone:** Cria uma cópia local de um repositório remoto.
  ```bash
  git clone <url_do_repositorio>
  Exemplo: git clone https://github.com/usuario/projeto.git
  ```

- **add:** Adiciona alterações ao índice (staging area) para o próximo commit.
  ```bash
  git add <arquivo_ou_diretorio>
  Exemplo: git add arquivo.txt
  ```

- **commit:** Registra as mudanças no repositório com uma mensagem descritiva.
  ```bash
  git commit -m "mensagem do commit"
  Exemplo: git commit -m "Adiciona nova funcionalidade"
  ```

- **push:** Envia os commits locais para o repositório remoto.
  ```bash
  git push <nome_remoto> <nome_branch>
  Exemplo: git push origin main
  ```

## Dicas Adicionais
- **Branches:** Use branches para desenvolver funcionalidades ou corrigir bugs de forma isolada.
  ```bash
  Criar nova branch: git checkout -b <nome_da_branch>
  Trocar de branch: git checkout <nome_da_branch>
  ```

- **Merge:** Combine alterações de diferentes branches.
  ```bash
  Fazer merge: git merge <nome_da_branch>
  ```

- **Status:** Verifique o estado do seu repositório.
  ```bash
  git status
  ```

- **Pull:** Atualize seu repositório local com as mudanças do remoto.
  ```bash
  git pull <nome_remoto> <nome_branch>
  ```

- **Log:** Veja o histórico de commits.
  ```bash
  git log or git log --oneline
  ```

- **Remotes:** Gerencie os repositórios remotos associados ao seu projeto.
  ```bash
  Adicionar remoto: git remote add <nome_remoto> <url_do_repositorio>
  Verificar remotos: git remote -v
  ```

- **Stash:** Salve alterações temporárias sem fazer commit.
  ```bash
  Salvar mudanças: git stash
  Restaurar mudanças: git stash pop
  ```

- **Rebase:** Reaplique commits em cima de outro branch.
  ```bash
  git rebase <branch_base>
  ```

## Comandos Importantes do Terminal
1. **ls:** Lista os arquivos e diretórios no diretório atual.
2. **cd:** Muda de diretório, ex: cd '/c/Users/carlens.oslin/Documents/Estudos/BACK/Git&Github'
3. **pwd:** Mostra o diretório atual.
4. **mkdir:** Cria novos diretórios.
5. **touch:** Cria novos arquivos vazios.
6. **cp:** Copia arquivos e diretórios.
7. **mv:** Move ou renomeia arquivos e diretórios.
8. **rm:** Exclui arquivos e diretórios.
9. **nano:** Editor de texto simples no terminal.
10. **cat:** Mostra o conteúdo de um arquivo.
11. **grep:** Pesquisa por padrões em arquivos.
12. **find:** Localiza arquivos em um sistema de arquivos.
13. **chmod:** Altera as permissões de acesso de arquivos e diretórios.
14. **chown:** Altera o proprietário e/ou grupo de um arquivo ou diretório.
15. **man:** Exibe o manual de um comando.
16. **cd ..** Voltar ao diretório anterior.

## Ordem de Operações com Git
1. Configurar nome e email do usuário no Git:
   ```bash
   git config --global user.name "user_name"
   git config --global user.email "user_email"
   ```
2. Criar um repositório:
   ```bash
   git init
   ```
3. Modificar arquivos.
4. Adicionar arquivos ao índice:
   ```bash
   git add nome_do_arquivo
   ```
5. Fazer commit das alterações:
   ```bash
   git commit -m "Descrição do commit"
   ```
6. Enviar alterações para o repositório remoto:
   ```bash
   git push <nome_remoto> <nome_branch>
   ```

## Passo a Passo de Configuração e Uso do Git

## parte01
1. Configurar nome e email:
   ```bash
   git config --global user.name "user_name"
   git config --global user.email "user_email"
   ```
2. Configurar VS Code como editor padrão:
   ```bash
   git config --global core.editor "code --wait"
   ```
3. Inicializar repositório:
   ```bash
   git init
   ```
4. Modificar arquivos.
5. Adicionar arquivos ao índice:
   ```bash
   git add nome_do_arquivo
   ```
6. Fazer commit:
   ```bash
   git commit -m "Primeiro commit"
   ```
7. Verificar histórico de commits:
   ```bash
   git log --oneline
   ```

### .gitignore
- **Definição:** Especifica arquivos/diretórios que Git deve ignorar.
- **Uso:** Evitar versionamento de arquivos desnecessários.
- **Exemplo:** Ignorar `.env`.

## Observação
- Todos os commits estão conectados ao commit anterior, exceto o primeiro commit.**
```

## parte02
- Git branch
A alternative timeline 
