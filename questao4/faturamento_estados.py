import json

# carregar o arquivo json com os dados
with open("faturamentoDosEstados.json") as file:
    dados = json.load(file)

# pegar o array de estados
vetor_faturamento = dados["faturmento_por_estado"]

valores = []
estados = []

## separando os valores e os estados
for estado in vetor_faturamento:
    valores.append(list(estado.values())[0])
    estados.append(list(estado.keys())[0])


soma_dos_valores = sum(valores)

for estado,valor in zip(estados,valores):
    porcentagem = (valor*100)/soma_dos_valores
    print(f"{estado} tem {porcentagem:.2f}% de representação no valor total que é = R${soma_dos_valores:.2f}")