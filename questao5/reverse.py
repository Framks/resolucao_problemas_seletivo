palavra = input("escreva uma palavra ou frase para reverte-la: ")

contrario = ""

for i in range(len(palavra)-1, -1, -1):
    contrario += palavra[i]


print(contrario)