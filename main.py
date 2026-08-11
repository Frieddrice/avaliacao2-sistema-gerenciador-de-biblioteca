import definicoes as d
d.limpa()
d.cabecalho() #Cabeçalho e sistema de limpeza do programa
import sys

livros = []

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
    print("FAÇA O CADASTRO AQUI!")
    titulo = str(input("Título do livro: "))
    autor = str(input ("Autor: "))
    ano = int(input("Ano de publicação: "))
    isbn = input("Código ISBN: ")
    status = "disponível"
    print(status)

    livro = {
        "título": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }

    livros.append (livro) #o append coloca esse dicionário na lista, e conforme novos livros vão sendo cadastrados, a lista vai crescendo

def emprestimo():
    while True:
        print("\nREGISTRE O SEU EMPRÉSTIMO AQUI!")
        print("Visualizar status dos livros:")
        titulo = input("Digite aqui o nome do livro que deseja encontrar: ")
        encontrado = False

        for livro in livros:
            if livro ['título'].lower() == titulo.lower():
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
                            print("\nEmpréstimo realizado com sucesso!\n")
                        elif opcao == "2":
                            print("Ok. Caso deseje realizar depois, volte aqui mais tarde!\n")
                        break
                else:
                    print("Este livro já está emprestado!")
                break
        if encontrado == False:
                        print("\nLivro não encontrado. Tente novamente!\n")
        if deseja_continuar() == True:
            break



def menu_principal(): #menu principal
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
        elif op == "4":
            print("Carregando a listagem de todos os livros...\n")
        elif op == "5":
            print("Carregando a função de busca....")
        elif op == "6":
            print("Carregando a função de ordenar listagem de livros...\n")
        elif op == "0":
            print("Encerrando Sistema...\n")
            break
        else:
            print("\nOpção inválida. Tente novamente!\n")
menu_principal() 

