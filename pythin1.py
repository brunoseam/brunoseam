#Algoritmo - > sequencia de passos para executar uma tarefa

#3 estrututas possiveis no algoritimo

#1 - estrutural *(sequência de passos contínuos)
#2 - condicional (DECISÃO - Vou execultar um script se conter o X e outro se Y)
#3 - Repetição - permite execultar varias vezes o mesmo codigo 

#variaveis 
#espaços de memoria que pode armazenar dados para execução de um processo!

#int float, string e boolean
#int : armazena valores inteiros (10, 14, 99, 365...)
#float (1.(ponto)11(valor quebrado)): Numeros decimais (1.2, 2.2, 4.1, 6,34... valor fracionádo)
#String (" ", '',): cadeia de caracteres: "Rua dos Bobos n 0" São valores literais, ou seja não vou fazer calculos. Ex, bruno, gustavo, kelvin... não fara calculos
#regras - > uma string deve estar string deve estar entre "", '', "house's Fer"
#boolean : é o polígrafo ele aceita dois valores true (verdadeiro) e false(falso)


#VARIAVEIS
# curso = "manufatura digital"
# #a variavel "curso" recebe o valor "manufatura digital"

# #exibir -> Comando Print
# print("Olá eu sou um print, estou executando seu py")

# #input = para conversar com o usuario. 
# altura = float(input("digite sua altura"))
# #a variavel altura recebe um valor quebrado de altura

# print(F"sua altura é {altura}")
# #exibe para mim a "FORMATAÇÃO" DO TEXTO COM O VALOR DE UMA VARIAVEL 

# nome = input("Digite seu nome")
# sobrenome = input("digite seu sobrenome")
# print (nome + sobrenome)

# print ("cadastro de uma pessoa")
# nome = input("digite seu nome")
# idade = input("Digite sua idade")
# endereço = input("Digite seu endereço")
# CPF = ("Digite seu CPF")
# distancia = input("digite sua disttancia")
# anodenascimento = input("Digite sua data de nascimento")
# print(nome, idade, endereço, CPF, distancia, anodenascimento)


#estrutura de algoritimo CONDICIONAL
#Executo alguma instrução de acordo com os dados que tenho. Por exemplo, só posso me alistar no exercito se for maior de idade
#Para usar o if e Else, eu tenho que saber quais as opções que tenho

# if(idade > 18):
#     print("Você já pode se alistar")
# else:
#     print("Você é menor idade")
    
# if(distancia <22):
#     print("você mora perto o suficiente")
# else:
#     print("você não pode entrar pois não esta perto o suficiente")



print ("Dados de um Salário")
salario = float (input("Digite seu salário"))

if (salario >= 1500):
    print(f"seu salário é{salario + 500}")

elif (salario >= 2000):
    print(f"seu salário é{salario + 400}")
    
elif (salario >= 2000):
    print(f"seu salário é{salario + 300}")

else:
    print("ótimo aumento")
    
    