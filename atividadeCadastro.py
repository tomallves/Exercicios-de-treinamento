from re import match

print("--------------MENU--------------")
quantidade = int(input("Quantos usuários serão cadastrados? "))
contador = 1

class Usuario():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def exibirMenu():
    print("\n1 - Cadastrar novo usuário \n2 - Lista de usuários cadastrados \n3 - Busca de usuário \n4 - Remoção de usuário \n5 - Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def buscaUser():
    busca = input("Nome: ")
    encontrado = False
    for i in lista:
        if i.nome == busca:
            print("\nUsário encontrado:")
            print(i.nome,",",i.idade, "anos")
            return True
            break    
    if not encontrado:
        print("Usuário não encontrado")

def removerUser():
    remov = input("Nome: ")
    encontrado = False
    for i in lista:
        if i.nome == remov:
            print("\nUsário removido")
            lista.remove(i)
            return True
    if not encontrado:
        print("Usuário não encontrado")

lista = []

while True:
    opcao = exibirMenu()
    if opcao == 1:
        if contador <= quantidade:
            print("\nNovo usuário")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            usuario = Usuario(nome.capitalize(), idade)
            lista.append(usuario)
            print("Usário cadastrado com sucesso!")
            contador += 1
        else:
            print("Quantidade excedida!")

    elif opcao == 2:
        print("\nLista de usuários:")
        n = 1
        for i in lista:
            print(f"{n}. ",i.nome, ",",i.idade, "anos")
            n = n + 1

    elif opcao == 3:
        print("\nBusca de usuário")
        busca = buscaUser()
        
    elif opcao == 4:
        print("\nRemover usuário")
        remov = removerUser()
        
    elif opcao == 5:
        break

    else:
        print("Opção inválida")