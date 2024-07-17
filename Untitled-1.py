# nome = input("digite o nome da empresa")

# empresa = input("digite o nome da empresa")

# serial = int(input("códico de barras"))

# kcal =float(input("números de kalorias"))

# volume = input("quantidade de volume a ser gasto")

# desig = input("Design a ser usado nas campanhas")

# fabricação = input("digite a data de sua fabricação")

# validade = input("comente sobre a validade do produto")

# receita = input("ingredientes a serem ultilizados")

# arm = input("onde será armazenada")

# quantidade = int(input("quantidade de embalagens a ser ultilizada"))

# preço = float(input("Valor do produto"))

produto = input("Bem vindo, diga logo o que deseja")
valordoproduto = float(input("informe o preço do produto"))
formadepag = float(input("qual seria sua forma de pagamento \n [1]-dinhero\n[2]-credito\[3]-debito\n[4]-pix"))

limite = 5555
senha = 333333
saldo = 1500

if formadepag == 1:
    din = float(input("qual o valor dado?"))
    if(din > valordoproduto):
        print("parabens peça sua compra, seu troco é", din - valordoproduto)
    elif(din == valordoproduto):
        print("PARABENS PELA SUA COMPRA!!!!")
    else:
        print("A COMPRA NÃO PFOI POSSIVEL")
elif formadepag == 2:
    if(limite >= valordoproduto):
        op = input(" Deseja parcelar sua compra? S - Sim ou N - Não")
        senhaUser = input("DIGITE SUA SENHA ")
        if(senhaUser == senha):
            if(op == "N"):
                print("Parabens pela sua compra")
            elif(op == "S"):
                nparcela = int(input("em quantas vezes deseja parcelar?"))
                print("Parabens pela sua compra, a parcela foi de ", valordoproduto/nparcela)
            else:
                print("O valor não é válido")
        else:
            print("Senha incorreta")
    else:
        print("o seu saldo é insuficiente")

elif formadepag == 3:
    if(saldo >= valordoproduto):
        print("")