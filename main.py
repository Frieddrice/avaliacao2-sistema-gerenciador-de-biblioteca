import definicoes as d
d.limpa()
d.cabecalho() #Cabeçalho e sistema de limpeza do programa
import sys
import csv

livros = [] #Lista vazia

def carregar_do_arquivo(): #traz do csv para o programa
    try: #peço para o phyton abrir o arquivo para ler
        with open ("livros.csv", mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                linha["ano"] = int(linha["ano"])
                livros.append(linha) #vai adicionando as coisas na lista conforme vai passando por elas
    except FileNotFoundError: 
        pass #se nenhum arquivo existir, ele apenas irá continuar

def salvar_em_arquivo():# manda de volta para o csv
    with open("livros.csv", mode="w", newline="",encoding="utf-8") as arquivo:
        colunas = ["título", "autor", "ano", "isbn", "status"]
        escritor = csv.DictWriter(arquivo, fieldnames = colunas)
        escritor.writeheader() #escreve as colunas na primeira linha
        for livro in livros:
            escritor.writerow(livro) #aqui, ele escreve uma linha para cada livro na lista livros, na forma do csv

def deseja_continuar():
    while True:
        opcao = input("\nDeseja voltar para o menu principal?\n1. Sim\n2. Não\n3. Sair\nDigite: ")
        if opcao == "1":
            return True

        elif opcao == "2":
            return False

        elif opcao == "3":
            sys.exit()

        else:
            print("Opção inválida. Tente novamente digitando 1, 2 ou 3!")



def cadastro():#Função cadastro
    print("\nFAÇA O CADASTRO AQUI!\n")
    while True:
        titulo = input("Título do livro: ").strip() #serve para limpar os spaços nas extremidades
        if titulo:
            break
        print("Erro! O título não pode estar com o campo vazio. Tente novamente!")
    while True:
        autor = input ("Autor: ").strip()
        if autor:
            break
        print("Erro! O nome do autor não pode estar com o campo vazio. Tente novamente!")
    while True:
        ano_str = input("Ano de publicação: ").strip()
        if ano_str.isdigit():
            ano = int(ano_str)
            if ano <=2026:
                break
            else:
                print("Ano inválido. Tente novamente!")
        else:
            print("Erro! O ano deve conter apenas números! tente novamente")
    while True:
        isbn = input("Código ISBN: ").strip()
        if isbn.isdigit() and len(isbn) == 13:
            break
        print("Erro! O ISBN deve conter 13 dígitos (apenas números)!")

    livro = { #Dicionário
        "título": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }
    livros.append(livro) #o append coloca esse dicionário na lista, e conforme novos livros vão sendo cadastrados, a lista vai crescendo
    salvar_em_arquivo()
    print("\nSalvamos o seu cadastro em nosso sistema!")

def emprestimo():
    while True:
        print("\nREGISTRE O SEU EMPRÉSTIMO AQUI!\n")
        titulo = input("Digite aqui o nome do livro que deseja encontrar: ").strip()
        if not titulo:
            print("O campo de busca não pode ficar vazio! Tente novamente.")
            continue
        encontrado = False

        for livro in livros:
            if titulo.lower() in livro['título'].lower():
                encontrado = True
                print(f"Livro encontrado!\n\nTítulo: {livro['título']}")
                print(f"Status atual: {livro['status']} ")
                if livro['status'] == "disponível":
                    while True:
                        op_validas = ["1" , "2"]
                        opcao= input("\nDeseja realizar um empréstimo?\n1. Sim\n2. Não\nDigite: ")
                        if opcao not in op_validas:
                            print("Opção inválida. Tente novamente!")
                            continue
                        if opcao == "1":
                            livro ['status'] = "emprestado"
                            salvar_em_arquivo()
                            print("\nEmpréstimo realizado com sucesso!\n")
                        elif opcao == "2":
                            print("Ok. Caso deseje realizar depois, volte aqui mais tarde!\n")
                        break
                else:
                    print("Este livro já está emprestado!")
                break
        if not encontrado:
                        print("\nLivro não encontrado. Tente novamente!\n")
        if deseja_continuar() == True:
            break

def devolucao():
    while True:
        op_validas = ["1" , "2"]
        print("\nFAÇA A SUA DEVOLUÇÃO AQUI!\n")
        titulo = input("Digite aqui o título do livro que deseja devolver: ").strip()
        if not titulo:
            print("O campo de busca não pode ficar vazio! Tente novamente.")
            continue
        encontrado = False
        for livro in livros:
            if titulo.lower() in livro['título'].lower():
                encontrado = True
                print(f"\nLivro encontrado: {livro['título']}")
                print(f"Status atual: {livro['status']}")
                if livro['status'] == "emprestado":
                    while True:
                        opcao = input("Você deseja realizar a devolução?\n1. Sim\n2. Não\nDigite: ")
                        if opcao not in op_validas:
                            print("Opção inválida. Tente novamente!")
                            continue
                        if opcao == "1":
                            livro['status'] = "disponível"
                            salvar_em_arquivo()
                            print(f"\nTítulo {livro['título']}\nDevolução realizada com sucesso!\n")
                        elif opcao == "2":
                            print("Devolução cancelada!")
                        break
                else:
                    print("Este livro já está disponível na biblioteca!")
                break
        if not encontrado:
            print("Livro não encontrado. Tente novamente!")

        if deseja_continuar() == True:
            break

def listar_livros():
    print("\nLISTA DE TODOS OS LIVROS:\n")
    if not livros:
        print("Nenhum livro foi cadastrado na biblioteca ainda!\n")
        return
    for livro in livros:
        print(f"Título: {livro['título']}\nStatus atual: {livro['status']}\n\n")

def buscar_livros():#função que encontra os livros
    print("\nPESQUISE POR SEUS LIVROS FAVORITOS AQUI!\n")
    nome_l =input("Por qual livro/autor você está procurando? ").strip().lower() #pergunta por qual livro o usuário está procurando
    encontrado = False #inicialmente dado como "falso" pois será encontrado
    for livro in livros:
        if nome_l in livro['título'].lower() or nome_l in livro['autor'].lower():#se o título do livro/autor digitado pela pessoa corresponder a algum que está salvo na tabela
            encontrado = True 
            print("\nLivro encontrado!") #ele será encontrado
            print("--------------------")
            print(f"Título: {livro['título']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Status: {livro['status']}") #informações sobre o livro desejado
            print("-----------------------------------------")
    if not encontrado:
        print("Nenhum livro encontrado! Tente novamente!") #caso não corresponder, o programa retorna como falso
        if deseja_continuar() == True: #função criada para dar continuidade ou não às atividades no sistema
            return

def ordenar_a_listagem():
    while True:
        print("FILTRE OS LIVROS POR:")
        print("1. título\n2. Autor\n3. Ano")
        escolha = input ("Digite aqui por qual opção você deseja filtrar: ")
        if escolha == "1":
            def por_titulo(livro):
                return livro['título'].lower()
            livros.sort(key = por_titulo)
            print("\nLivros ordenados por título:\n")
        elif escolha == "2":
            def por_autor(livro):
                return livro['autor'].lower()
            livros.sort(key = por_autor)
            print("\nLivros ordenados por Autor:\n")
        elif escolha == "3":
            def por_ano(livro):
                return livro['ano']
            livros.sort(key = por_ano)
            print("\nLivros ordenados por Ano:\n")
        elif escolha == "0":
            print("Opção inválida!")
            break
        else: 
            print("\nOpção inválida!\n")
            continue
        for livro in livros:
            print(f"\n\nTítulo: {livro['título']}\nAutor: {livro['autor']}\nAno: {livro['ano']}")
        if deseja_continuar() == True:
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
            break
        else:
            print("\nOpção inválida. Tente novamente!\n")
menu_principal() 