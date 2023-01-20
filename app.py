


lista=[]

while True:
    print("Escolha uma opção:")
    opcao=input("[i]nserir, [a]pagar, [l]istar \n")
    if opcao=="i":
        objeto=input("Digite o nome do objeto: \n")
        lista.append(objeto)
    elif opcao=="l":
        if len(lista)>0:
            for counter,value in enumerate(lista,1):
                print(counter, value)
        else:
            print("Lista inexistente")
    elif opcao=="a":
        apagar=input("Escolha qual item deletar: \n")
        for i in enumerate(lista,1):
            if i==apagar:
                lista.remove(i)
            else:
                print("Item não identificado")
    else:
        print("Escolha uma das opções descritas")
        opcao=input("[i]nserir, [a]pagar, [l]istar \n")


