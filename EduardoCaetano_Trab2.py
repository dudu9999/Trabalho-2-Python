# Autor: Eduardo Caetano.
# Turma: Sexta Feira.
# Sexta Sala: 601.

# LISTAS
preco_unitário = 0
listaDeProdutos = []
listaDeQuantidades = []
listaDePrecos = []
no_carrinho = []

# VARIAVEIS
produto = " "
escolha2,escolha3 = 0, 0

st   = "\n---------------------------------------------------------";
st += "\n                 MENU";
st += "\n---------------------------------------------------------";
st += "\n0- Fim";
st += "\n1- Cadastra Produtos";
st += "\n2- Confere Lista de Produtos";
st += "\n3- Confirma Produto";
st += "\n4- Mostra Total a pagar";
st += "\n---------------------------------------------------------";
st += "\nEscolha uma opção: ";
print()

while True:
    escolha = input(st)
    if escolha == '1':
        print("Lista de produtos")
        while True:
            produto = input("\n[Enter volta ao menu]\n...Digite o produto: ")
            quantidade = input("\n[Enter volta ao menu]\n...Digite a quantidade: ")
            if len(produto) == 0:
                break
            listaDeProdutos.append(produto)
            listaDeQuantidades.append(int(quantidade))
            no_carrinho.append(str("---"))
            #listaDeProdutos = listaDeProdutos.append(produto)

    if escolha == '2':
        
        ind = 0
        print("Deseja Adicionar algum produto no CARRINHO ?")        
        escolha2 = int(input("1 - Adicionar no carrinho // 2 - Ver a lista: "))
        print("---------------------------------------------------------------------------------------------------")
        if escolha2 == 1:
            for elemento in listaDeProdutos:
                print(ind," - [ Produto: "+str(elemento)+" - quantidade",listaDeQuantidades[ind]," ] - ",no_carrinho[ind])
                ind += 1
            print()    
            escolha3 = int(input("Qual numero do produto que deseja adicionar: "))
            for x in range(len(listaDeProdutos)):
                if escolha3 == x:
                    no_carrinho[x] = "OK"
                    
            print("---------------------------------------------------------------------------------------------------")
            for x in range(len(listaDeProdutos)):
                print(ind," - [ Produto: ",listaDeProdutos[x]," - quantidade",listaDeQuantidades[x]," ] - ",no_carrinho[x])
                
        elif escolha2 == 2:
            for elemento in listaDeProdutos:
                print(ind," - [ Produto: "+str(elemento)+" - quantidade",listaDeQuantidades[ind]," ] - ",no_carrinho[ind])
                ind += 1      

    if escolha == '3':
        soma = 0
        for e in listaDeProdutos:
            soma += e
        print("Soma: ",soma)
        
        print("Soma: ",sum(listaDeProdutos))

    if escolha == '4':
        if len(listaDeProdutos) > 0:
            print("Média calculada: ",sum(listaDeProdutos)/len(listaDeProdutos))

    if escolha == '5':
        for e in listaDeProdutos:
            if e%2 == 0:
                print("[",e,"]")
                
    if escolha == '6':
        for i in range(0,len(listaDeProdutos),1):
            if i%2 == 0:
                print(i,"-",listaDeProdutos[i])
        
        for i in range(0,len(listaDeProdutos),2):
            print(i,"-",listaDeProdutos[i])


    if escolha == '7':
        outraLista = []
        for e in listaDeProdutos:
            if e%2 == 1:
                outraLista.append(e)

    if escolha == '8':
        while True:
            try:
                num = int(input("Digite o número para localizar: "))
                break
            except:
                print("ERRO.")

        for i in range(len(listaDeProdutos)):
            if listaDeProdutos[i] == num:
                print("O número: ",num,"está na posição,",i,"da lista")

    if escolha == '9':
        while True:
            try:
                ind = int(input("Digite o indice para localizar: "))
                if ind >= 0 and ind < len(listaDeProdutos):
                    break
            except:
                print("ERRO.")

        print("O indice: ",ind,"corresponde ao número",listaDeProdutos[ind])



