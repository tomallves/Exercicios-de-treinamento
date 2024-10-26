lista = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]
ifinal = len(lista) - 1
inicio = 0
max = 20

def exibirMenu():
    print(">>> MENU DE OREDENAÇÃO <<<")
    print("1 - Adicionar elemento \n2 - BubbleSort \n3 - MergeSort  \n4 - Listar \n5 - Remover elemento \n6 - Vazia \n7 - Sair")
    opcao = int(input("Escolha uma opção (1-4): "))
    return opcao

def vazia():
    if ifinal == -1:
        return True
    else:
        return False
    
def BubbleSort():
    for i in range(0, len(lista) -1):
        for j in range(len(lista) -1):
            if lista[j] > lista[j+1]:
                inicio = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = inicio
    return lista

def MergeSort():
    ifinal = len(lista) - 1

    for patual in range(0, ifinal):
        pmenor = patual
        menor = lista[pmenor]

        for buscap in range(patual, ifinal):
            busca = lista[buscap + 1]

            if menor > busca:
                menor = busca
                pmenor =  buscap + 1

        if pmenor != patual:
            menor = lista[pmenor]
            lista[pmenor] = lista[patual]
            lista[patual] = menor

    return lista

while True:
    opcao = exibirMenu()
    if opcao == 1: 
        if len(lista) < max:
            ifinal += 1
            coisa = int(input("\nElemento: "))
            lista.append(coisa)
        else: 
            print("\nLista cheia!\n")

    elif opcao == 2: 
        if not vazia():
            BubbleSort()
            print("\nLista na ordem crescente:\n",lista,"\n")
        else:
            print("\nLista vazia")

    elif opcao == 3:
        if not vazia():
            MergeSort()
            print("\nLista na ordem crescente:\n",lista,"\n")
        else:
            print("\nLista vazia")
            
    elif opcao == 4:
        print("\nElementos da lista:")
        if not vazia():
            for i in lista:
                print(i)
        else:
            print("\nLista vazia")

    elif opcao == 5:
        if not vazia():
            x = int(input("Remover: "))
            if x in lista:
                lista.remove(x)
            else:
                print("Elemento não está na lista")
        else:
            print("\nLista vazia")

    elif opcao == 6:
        print(ifinal)
        if not vazia():
            print("\nLista cheia\n") 
        else:
            print("\nLista vazia\n") 
    
    elif opcao == 7:
        break
    
    else:
        print("Opçao inválida")