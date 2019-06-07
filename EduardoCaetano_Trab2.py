# Autor: Eduardo Caetano.
# Turma: Sexta Feira.
# Sexta Sala: 601.

#imports
import sys

# LISTAS
listaDeProdutos = []
listaDeQuantidades = []
listaDePrecos = []
no_carrinho = []

# VARIAVEIS
produto, num, texto = " ", " ",""
escolha2, escolha3, escolha4 = 0, 0, 0
preco, resultado = 0.0,  0.0

## Função para ler um inteiro #######################################################################

def lerInteiro(mens): 
    while True:
        try:
            n = int(input(mens))            
            return n
        except:
            input("...Erro. Você não digitou um número inteiro.")
            
## Função para ler um Texto #######################################################################
            
def lerstring(mensS):
    while True:
        try:
            n = str(input(mensS))
            return n
        except:
            input("...Erro. Você não digitou letras.")
            
## Função para ler um float (Preço) ###################################################################            
def lerfloat(mensS):
    while True:
        try:
            n = float(input(mensS))
            return n
        except:
            input("...Erro. Você não digitou um número quebrado EX: 2.50.")
            
## Função para mostrar a lista #######################################################################
            
def mostraLista(listaDeProdutos):
    ind = 0
    for x in range(len(listaDeProdutos)):
        print(ind," - [ Produto: ",listaDeProdutos[x]," - Quantidade:",listaDeQuantidades[x]," - Preço: R$ ",listaDePrecos[x]," ] - ",no_carrinho[x])
        ind += 1
    print("---------------------------------------------------------------------------------------------------")

## Função para mostrar o menu #######################
def mostraMenu(st):
    st   = "\n-----------------------------------------------------------";
    st += "\n|                   MENU                           |";
    st += "\n|---------------------------------------------------------|";
    st += "\n| 0- Fim                                             |";
    st += "\n| 1- Cadastra Produtos                  |";
    st += "\n| 2- Confere Lista de Produtos     |";
    st += "\n| 3- Confirma Produto                    |";
    st += "\n| 4- Mostra Total a pagar              |";
    st += "\n----------------------------------------------------------";
    print(st)
    
## Função para fazer a escolha no menu ###############################################################
    
def menu(escolha):
    if escolha == '0' :
        print()
        print("Ate logo!")
        sys.exit()
        
    if escolha == '1':
        print()
        print("------ Cadastro de produtos ------")
        while True:
            produto       = lerstring("\n[Aperte ENTER para voltar ao menu]\nDigite o nome produto: ")
            if produto == "":
                break

            quantidade = lerInteiro("\n[Digite 0 e aperte ENTER para voltar ao menu]\nDigite a quantidade: ")
            if quantidade == 0:
                break
            
            listaDeProdutos.append(produto)
            listaDeQuantidades.append(int(quantidade))
            no_carrinho.append(str("---"))
            listaDePrecos.append(float(preco))
            #listaDeProdutos = listaDeProdutos.append(produto) #lista dentro de lista
            
    ###############################################################################################
            
    if escolha == '2':
        while True:
            if len(listaDeProdutos) == 0:
                print("Lista VAZIA!")
                break
            
            print()
            ind = 0        
            escolha2 = lerInteiro("Deseja Adicionar algum produto no CARRINHO ?\n1 - Adicionar no carrinho\n2 - Ver a lista e voltar para o menu: ")
            print() 
            if escolha2 == 1:
                print("---------------------------------------------------------------------------------------------------")
                mostraLista(listaDeProdutos)
                print()    
                escolha3 = lerInteiro("Qual numero do produto que deseja adicionar: ")
                
                for x in range(len(listaDeProdutos)):
                    if escolha3 == x:
                        no_carrinho[x] = "OK"
                        
                print()                    
                print("------ lista de produtos atualizada -----------------------------------------")
                mostraLista(listaDeProdutos)
                break

            elif escolha2 == 2:
                print("---------------------------------------------------------------------------------------------------")
                mostraLista(listaDeProdutos)
                break
                
    ###############################################################################################
            
    if escolha == '3':
        while True:
            if len(listaDeProdutos) == 0:
                print("Lista VAZIA!")
                break
            contador = 0
            for x in range(len(listaDeProdutos)):
                if no_carrinho[x] == "---":
                    contador += 1
            if contador == len(listaDeProdutos):
                print("Lista VAZIA!")
                break
            
            print()
            print("---------------------------------------------------------------------------------------------------")
            ind = 0
            for x in range(len(listaDeProdutos)):
                if no_carrinho[x] == "OK":
                    print(ind," - [ Produto: ",listaDeProdutos[x]," - Quantidade:",listaDeQuantidades[x]," - Preço: R$ ",listaDePrecos[x]," ] - ",no_carrinho[x])
                              
                ind += 1
            print("---------------------------------------------------------------------------------------------------")
            print()
        
            escolha3 = lerInteiro("Qual produto que deseja adicionar o preço: ")
            if escolha3 > (len(listaDeProdutos)-1):
                print("Numero maior que o que consta na lista")
                break
                
            for x in range(len(listaDeProdutos)):
                if no_carrinho[escolha3] == "OK":
                    for x in range(len(listaDeProdutos)):
                        if escolha3 == x:
                            listaDePrecos[x] = lerfloat("Digite o preço do produto: ")
                    print("Preço Adicionado")
                    break    
                else:
                    print("Esse produto não esta no carrinho!")

            print()                    
            print("------ lista de produtos atualizada -----------------------------------------")
            mostraLista(listaDeProdutos)
            break   
                
                
                
    ###############################################################################################
                
    if escolha == '4':
        print()
        print("--- Itens que vão ser comprados -----------------------------------------")
        ind = 0
        for x in range(len(listaDeProdutos)):
            if no_carrinho[x] == "OK":
                print(ind," - [ Produto: ",listaDeProdutos[x]," - Quantidade:",listaDeQuantidades[x]," - Preço: R$ ",listaDePrecos[x]," ] - ",no_carrinho[x])
            ind += 1
        print("---------------------------------------------------------------------------------------------------")
        print()

        print("--- Itens que não vão ser comprados ----------------------------------")
        ind, cont = 0, 0
        for x in range(len(listaDeProdutos)):
            if no_carrinho[x] != "OK":
                print(ind," - [ Produto: ",listaDeProdutos[x]," - Quantidade:",listaDeQuantidades[x]," - Preço: R$ ",listaDePrecos[x]," ] - ",no_carrinho[x])
            ind += 1
        print("---------------------------------------------------------------------------------------------------")
        print() 
        resultado = 0
        for x in range(len(listaDeProdutos)):        
            if no_carrinho[x] == "OK":
                cont += 1
                resultado = (resultado + (listaDeQuantidades[x]*listaDePrecos[x]))
        if cont == 1:
            print("Você vai gastar: R$",resultado,"\nPara comprar esse prrodutos")
            sys.exit()
        else:
            print("Você vai gastar: R$",resultado,"\nPara comprar esses ",cont," prrodutos")
            sys.exit()
                    
### EXECUÇÂO ####################################################################################
        
while True:
    mostraMenu(texto)
       
    menu(lerstring("Escolha uma opção: "))

   
