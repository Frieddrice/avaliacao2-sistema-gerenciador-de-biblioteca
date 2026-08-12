import definicoes as d
d.limpa()
d.cabecalho() #Cabeçalho e sistema de limpeza do programa
import sys
import csv

livros = [] #Lista vazia

def carregar_do_arquivo(): #traz do csv para o programa
    try: #Aqui, o sistema tenta executar o código que está aqui embaixco
        with open ("livros.csv", mode="r", encoding="utf-8") as arquivo:#Peço para o python abrir a lista no modo read (apenas para leitura)
            leitor = csv.DictReader(arquivo) #O Dict.Reader lê cada linha do CSV e transforma em dicionário
            for linha in leitor:
                linha["ano"] = int(linha["ano"]) #Pega os números que estavam como string (texto) e "transforma" em números inteiros
                livros.append(linha) #vai adicionando as coisas na lista conforme vai "corrigindo"
    except FileNotFoundError: 
        pass #se nenhum arquivo existir, ele apenas irá continuar

def salvar_em_arquivo():# função que salva tudo para que mesmo que o programa feche, os dados continuem salvos
    with open("livros.csv", mode="w", newline="",encoding="utf-8") as arquivo: #Agora, as coisas abaixo são adicionadas no modo write (escrita)
        colunas = ["título", "autor", "ano", "isbn", "status"] #Aqui, se trata da organização da lista, como se fossem os títulos
        escritor = csv.DictWriter(arquivo, fieldnames = colunas)
        escritor.writeheader() #escreve as colunas na primeira linha
        for livro in livros:
            escritor.writerow(livro) #aqui, ele escreve uma linha para cada livro na lista livros, na forma do csv

def deseja_continuar(): #Mini def que aparece no final de todas as funções
    while True:
        opcao = input("\nDeseja voltar para o menu principal?\n1. Sim\n2. Não\n3. Sair\nDigite: ")
        if opcao == "1": #Se a opção do usuário for igual a 1, ela retorna como True, ou seja, volta ao menu principal
            return True

        elif opcao == "2": #Caso não deseje, ela retornará como False, e a função no qual o usuário está se repete
            return False

        elif opcao == "3": #Aqui, o usuário consegue sair do sistema caso ele deseje
            sys.exit()

        else: #Caso o usuário digitar outra opção que não estiver nas fornecidas inicialmente, o sistema informará que ela é inválida
            print("Opção inválida. Tente novamente digitando 1, 2 ou 3!")



def cadastro():#Função cadastro
    print("\nFAÇA O CADASTRO AQUI!\n")
    while True:
        titulo = input("Título do livro: ").strip() # o strip serve para limpar os espaços nas extremidades
        if titulo: #Se o campo do título não estiver vazio, ele aceita
            break
        print("Erro! O título não pode estar com o campo vazio. Tente novamente!") #Printa como erro
    while True:
        autor = input ("Autor: ").strip()  
        if autor: #Se o campo do autor não estiver vazio, ele aceita
            break
        print("Erro! O nome do autor não pode estar com o campo vazio. Tente novamente!") #Printa como erro também
    while True:
        ano_str = input("Ano de publicação: ").strip()
        if ano_str.isdigit(): 
            ano = int(ano_str) # Uma nova variável ano vai ser igualada à modificação do ano em string (texto), pra um número int (inteiro)
            if ano <=2026: 
                break #Se o ano for menor do que 2026 (Ano atual), ele para, ou seja, aceita
            else:
                print("Ano inválido. Tente novamente!") #Senão, ele dá como inválido
        else:  #Aqui é um else para caso a pessoa tente digitar letras ao invés de números
            print("Erro! O ano deve conter apenas números! tente novamente")
    while True:
        isbn = input("Código ISBN: ").strip() #Aqui, eu igualei a variável do isbn ao que o usuário vai digitar
        if isbn.isdigit() and len(isbn) == 13: #O programa verifica se todos os caracteres presentes são númericos e lê um len, que indica o tamanho que deve conter
            break
        print("Erro! O ISBN deve conter 13 dígitos (apenas números)!")

    livro = { #Dicionário de cada livro da lista de livros
        "título": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }
    livros.append(livro) #O append coloca esse dicionário na lista, e conforme novos livros vão sendo cadastrados, a lista vai crescendo
    salvar_em_arquivo() #Ele salva os novos cadastros de livros na lista do csv
    print("\nSalvamos o seu cadastro em nosso sistema!")

def emprestimo():
    while True:
        print("\nREGISTRE O SEU EMPRÉSTIMO AQUI!\n")
        titulo = input("Digite aqui o nome do livro que deseja encontrar: ").strip() #O strip limpa os espaços vazios das extremidades 
        if not titulo: #Se não houver nada, o sistema sinaliza que o campo não pode ficar vazio
            print("O campo de busca não pode ficar vazio! Tente novamente.")
            continue #E volta para o loop
        encontrado = False #A variável encontrada vai ser False, pois queremos encontrá-la

        for livro in livros: 
            if titulo.lower() in livro['título'].lower(): #Se o título digitado pelo usuário estiver dentro da lista de livros na área de título,
                encontrado = True #O livro é encontrado
                print(f"Livro encontrado!\n\nTítulo: {livro['título']}")
                print(f"Status atual: {livro['status']} ")
                if livro['status'] == "disponível": 
                    while True:
                        op_validas = ["1" , "2"] #Eu fiz uma mini listinha das opções que podem ser escolhidas para fazer o empréstimo oun não
                        opcao= input("\nDeseja realizar um empréstimo?\n1. Sim\n2. Não\nDigite: ")
                        if opcao not in op_validas:#Se a opção digitada pelo usuário não estiver dentro da listinha, o sistema informa que a opção é inválida
                            print("Opção inválida. Tente novamente!")
                            continue #E volta ao inicio do loop
                        if opcao == "1": #Caso ele queira realizar o empréstimo
                            livro ['status'] = "emprestado"
                            salvar_em_arquivo() #O sistema muda o status para "emprestado" e salva essa alteração chamando a def
                            print("\nEmpréstimo realizado com sucesso!\n")
                        elif opcao == "2":#Caso ele não queira, essa função para
                            print("Ok. Caso deseje realizar depois, volte aqui mais tarde!\n")
                        break
                else: #Se o livro estiver emprestado, o programa irá avisar
                    print("Este livro já está emprestado!")
                break
        if not encontrado: #Se o livro não for encontrado, ou seja,continuar retornando False, o sistema informa também
            print("\nLivro não encontrado. Tente novamente!\n")
        if deseja_continuar() == True: #Mini def para continuar ou retornar, que se for verdade, dá break e retorna ao menu inicial
            break

def devolucao():
    while True:
        op_validas = ["1" , "2"]
        print("\nFAÇA A SUA DEVOLUÇÃO AQUI!\n")
        titulo = input("Digite aqui o título do livro que deseja devolver: ").strip() #Strip serve para limpar os espaços vazios que podem ficar nas extremidades na hora de digitar
        if not titulo: #Se não houver nada, o sistema sinaliza que o campo não pode ficar vazio
            print("O campo de busca não pode ficar vazio! Tente novamente.")
            continue
        encontrado = False #Inicialmente, a variável encontrada vai ser False, pois queremos encontrá-la
        for livro in livros:
            if titulo.lower() in livro['título'].lower(): #Se o título que o usuário escrever estiver na área dos títulos na lista de livros,
                encontrado = True #O livro específico é encontrado
                print(f"\nLivro encontrado: {livro['título']}")
                print(f"Status atual: {livro['status']}")
                if livro['status'] == "emprestado": #Se o status do livro estiver como "emprestado"
                    while True:
                        opcao = input("Você deseja realizar a devolução?\n1. Sim\n2. Não\nDigite: ") #E a pessoa digitar que quer realizar a devolução,
                        if opcao not in op_validas:
                            print("Opção inválida. Tente novamente!")
                            continue
                        if opcao == "1":
                            livro['status'] = "disponível" #O status muda para disponível
                            salvar_em_arquivo() #E essa alteração é salva na função de salvamento
                            print(f"\nTítulo {livro['título']}\nDevolução realizada com sucesso!\n")
                        elif opcao == "2": #Caso não queira realizar a devolução, nada muda
                            print("Devolução cancelada!")
                        break #e a função para
                else: #Caso o status não estiver como emprestado, ele informa que já está disponível na biblioteca
                    print("Este livro já está disponível na biblioteca!")
                break
        if not encontrado: #Se o livro continuar retornando False, o sistema informa que ele não foi encontrado
            print("Livro não encontrado. Tente novamente!")

        if deseja_continuar() == True: #Mini def para continuar ou retornar
            break

def listar_livros():
    print("\nLISTA DE TODOS OS LIVROS:\n")
    if not livros: #Se a lista livros retornar False, ou seja, não for encontrada, o sistema informa
        print("Nenhum livro foi cadastrado na biblioteca ainda!\n")
        return #E retorna
    for livro in livros: #Caso retorne True, ele informa todos os dados do livro (os mesmos q aparecem no cadastro)
        print(f"Título: {livro['título']}\nStatus atual: {livro['status']}\n\n")

def buscar_livros():#função que encontra os livros
    while True:
        print("\nPESQUISE POR SEUS LIVROS FAVORITOS AQUI!\n")
        nome_l =input("Por qual livro/autor você está procurando? ").strip().lower() #pergunta por qual livro o usuário está procurando. Obs: esse lower serve para "padronizar" o tipo da fonte (deixar tudo minúsculo)
        if not nome_l:
            print("O campo de busca não pode ficar vazio! Tente novamente.")
            continue
        encontrado = False #inicialmente dado como "falso" pois será encontrado
        for livro in livros:
            if nome_l in livro['título'].lower() or nome_l in livro['autor'].lower():#se o título do livro/autor digitado pela pessoa corresponder a algum que está salvo na tabela
                encontrado = True #Encontrado vai retornar como True, então 
                print("\nLivro encontrado!") #ele será encontrado
                print("--------------------")
                print(f"Título: {livro['título']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']}")
                print(f"Status: {livro['status']}") #informações sobre o livro desejado
                print("-----------------------------------------")
        if not encontrado: #Se o livro continuar retornando False
            print("Nenhum livro encontrado! Tente novamente!") #O sistema printa que ele não foi encontrado
        if deseja_continuar() == True: #função criada para dar continuidade ou não às atividades no sistema
                break #E para

def ordenar_a_listagem():
    while True:
        print("FILTRE OS LIVROS POR:")
        print("1. título\n2. Autor\n3. Ano") #Opções disponíveis para a filtragem
        escolha = input ("Digite aqui por qual opção você deseja filtrar: ")
        if escolha == "1": #Se a escolha for igual a 1, ou seja, o usuário escolher filtrar por título,
            def por_titulo(livro):
                return livro['título'].lower()
            livros.sort(key = por_titulo) #Aqui, o .sort serve para sinalizar ao sistema, que ele precisa organizar a lista por ordem, porém, comose trata de uma lista de dicionários, o "Key" serve como chave para indicar para onde o sistema deve "olhar", na hora de organizar
            print("\nLivros ordenados por título:\n")
        elif escolha == "2": #Aqui é basicamente a mesma lógica da def de cima, porém o key muda para "autor"
            def por_autor(livro):
                return livro['autor'].lower()
            livros.sort(key = por_autor)
            print("\nLivros ordenados por Autor:\n")
        elif escolha == "3": #E aqui tbm, só muda o key para "ano"
            def por_ano(livro):
                return livro['ano']
            livros.sort(key = por_ano)
            print("\nLivros ordenados por Ano:\n")

        else: 
            print("\nOpção inválida!\n")
            continue
        for livro in livros: #Parte onde aparece tudo organizado dependendo de como a pessoa escolheu listar
            print(f"\n\nTítulo: {livro['título']}\nAutor: {livro['autor']}\nAno: {livro['ano']}")
        if deseja_continuar() == True: #Mini def para a pessoa decidir se quer continuar, voltar ou sair do sistema
                break

def menu_principal(): #menu principal
    carregar_do_arquivo()
    while True: #sistema de loop
        print ("\n------------------------\nSISTEMA DE GERENCIAMENTO DE BIBLIOTECA\n---------------------------------------")
        print("1. Cadastrar livros")
        print("2. Registrar empréstimo de um livro ")
        print("3. Registrar devolução")
        print("4. Listar todos os livros ")
        print("5. Buscar um livro")
        print("6. Ordenar a listagem de livros")
        print("0. Fechar o sistema") #opções disponíveis para o usuário
        op = input("Digite qual função você deseja executar: ") #o programa pergunta o que o usuário deseja fazer
        if op == "1":
            print("\nCarregando a função cadastro...\n")
            cadastro()
        elif op == "2":
            print("\nCarregando a função empréstimo...\n")
            emprestimo()
        elif op == "3":
            print("\nCarregando a função de devolução...\n")
            devolucao()
        elif op == "4":
            listar_livros()
            print("\nCarregando a listagem de todos os livros...\n")
        elif op == "5":
            print("\nCarregando a função de busca....")
            buscar_livros()
        elif op == "6":
            ordenar_a_listagem()
            print("\nCarregando a função de ordenar listagem de livros...\n")
        elif op == "0":
            print("\nEncerrando Sistema...\n")
            break #Do 1 ao 0 são todas as opções disponíveis
        else: #Caso o usuário tente digitar qualquer outro número fora das opções, o sistema informará que a opção é inválida
            print("\nOpção inválida. Tente novamente!\n")
menu_principal() 