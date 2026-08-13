--- Feito por: Melyssa de Souza ALavrenga - 2°A-EM ---
----- Sistema de Gerenciamento de Biblioteca -----

Desenvolvido em Python, esse sistema controla por completo um acervo bibliotecário, com persistência de dados em formato .CSV e navegação interativa via terminal.

# Arquivos presentes:
 - README.md (explicação de como o programa funciona e suas características)
 - main.py (local onde se encontra o código por completo)
 - livros.csv (salva os livros cadastrados no sistema)

------------------
# Como usar:
• Primeiro, certifique-se de que você estará utilizando ou o Python 3.12 (que é a versão utilizada pelo programa) ou qualquer outra recente.
   Segundo, clone o repositório no seu pc utilizando o comando `git clone` seguido pelo link do projeto.
   Terceiro, Abra o terminal na pasta do diretório do projeto e execute o arquivo principal (`main.py`), É nele que o código está e onde tudo funciona.
   Quarto, Siga as instruções exibidas no terminal.
   !Obs: O arquivo `livros.csv` (que é responsável pela persistência dos dados) será criado ou atualizado automaticamente na pasta do projeto conforme você for cadastrando, emprestando ou devolvendo livros.
   O arquivo também já inicia com algumas obras cadastradas.

------------------
# Funcionalidades:
-------------------------------------------------------------------------------------------
 - Cadastrar livros: Permite adicionar novas obras informando título, autor, ano de publicação e código ISBN (com validação de 13 dígitos numéricos).
-------------------------------------------------------------------------------------------
 - Registrar empréstimo: Altera o status de um livro disponível para "emprestado" caso o leitor deseje desfrutar de uma leitura específica.
-------------------------------------------------------------------------------------------
 - Registrar devolução: Atualiza o status de um livro emprestado de volta para "disponível".
-------------------------------------------------------------------------------------------
 - Listar todos os livros: Exibe o catálogo completo com os dados e status atuais de cada obra cadastrada.
-------------------------------------------------------------------------------------------
 - Buscar um livro: Realiza buscas por parte do título ou do nome do autor.
-------------------------------------------------------------------------------------------
 - Ordenar a listagem: Organiza dinamicamente o acervo por título, autor ou ano de publicação (Fica a critério do usuário) utilizando algoritmos de ordenação em memória.
 ------------------------------------------------------------------------------------------
  - Fechar o Sistema: Encerra as atividades do programa.

# Observações importantes sobre requisitos técnicos:
 - Conhecimento prévio/intermediário sobre a linguagem Python
 - Familiaridade com o GitHub
 - Manipulação de arquivos (ex: csv)
 - Interpretação e uso correto do terminal