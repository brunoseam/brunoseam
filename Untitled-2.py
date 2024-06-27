numero =int(input("me escreva um número"))

if (numero%2 ==0):
    print ("Número par")
else:
    print ("Número impar")

if (numero> 0):
    print ("número positivo")
else:
    print ("número negativo")


valor1 = int(input("digite um valor"))
valor2 = int(input("digite um valor"))

if (valor1 == valor2):
    print ("números iguais")
else:
    print ("esses números não são iguais")

valor3 = int(input("degite um valor"))
          
if (valor3 >= 25 and valor3 <= 37) :
    print ("Este número aparece de 25 a 37")
else:
    print ("esse número não esta entre 25 a 37")

número3 = int(input("digite o número que deseja saber"))
número4 = int(input("digite um segundo número"))

if(número3 % número4 == 0 or número4 % número3 == 0):
    print("este número encontra seu múltiplo")
else:
    print("não são múltiplos")


number1 = int(input("digite um valor"))
number2 = int(input("digite um valor"))
number3 = int(input("digite um valor"))
number4 = int(input("digite um valor"))

if (number1 > number2 and number1 > number3 and number1 > number4):
    print ("o primeiro número é o maior")

elif (number2 > number1 and number2 > number3 and number2 > number4):
    print ("o segundo número é o maior")

elif (number3 > number1 and number3 > number2 and number3 > number4):
    print ("o terceiro número é o maior")

elif (number4 > number1 and number4 > number2 and number4 > number3):
    print ("o quarto número é o maior")
else:
    print ("existem mais de um número que são os maiores")

quantia1 = int(input("me escreva uma quantia"))
quantia2 = int(input("me escreva uma quantia"))
quantia3 = int(input("me escreva uma quantia"))
quantia4 = int(input("me escreva uma quantia"))

total = quantia1 + quantia2 + quantia3 + quantia4

print(f"o resultado dessa soma seria {total}")


quantidade1 = int(input("digite um número a calcular"))
quantidade2 = int(input("digite um número a calcular"))

result = quantidade1 % quantidade2

print(f"o resuldado da divisão é de: {result}")

quantidade3 = int(input("digite um número a calcular"))
quantidade4 = int(input("digite um número a calcular"))

result = quantidade3 ** quantidade4

print(f"o resuldado de sua potência é de: {result}")


altura1 = float(input("me fale uma altura"))
altura2 = float(input("me fale uma altura"))
altura3 = float(input("me fale uma altura"))


soma = altura1 + altura2 + altura3 
print(f"a mediana seria {soma / 3}")

val1 = int(input("me de unma temperatura em fahrenheit: "))

cel =  (val1 - 32) * 5/9
print(f'essa temperatura em célcius é de {cel}')

salário = float(input("me diga o seu salário"))
desconto = float(input("agora me fale o valor que foi descontado"))

salarioliquido = salário - desconto or desconto - salário
print(f"salário a receber: {salarioliquido}")

distancia = float(input("qual a distância percorrida?"))
tempo = float(input("e quanto tempo gasto"))

velocidademedia = distancia / tempo 

print(f"A velocidade Média seria de: {velocidademedia}")