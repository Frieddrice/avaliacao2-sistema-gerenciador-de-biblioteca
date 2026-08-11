import definicoes as d
d.limpa()
d.cabecalho() #Cabeçalho e sistema de limpeza do programa
import sys

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
            emprestimo()#Obs:chamei as defs antes de faze-las só para me organizar melhor dps!
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
menu_principal()#chama