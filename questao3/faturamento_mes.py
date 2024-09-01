import json

## bucando o json
with open("faturamento.json") as file:
    dados = json.load(file)

faturamento = []

## pegando os faturamentos diarios
for diario in dados["faturamento_diario"]:
    if(diario != 0):
        faturamento.append(diario)


## calculando o menor, maior, e a media
menor_diaria = min(faturamento)
maior_diaria = max(faturamento)
media = sum(faturamento) / len(faturamento)

## somatorio para saber quantos estão acima da media
dias_acima_media = sum(1 for diario in faturamento if diario > media)

print(f"Menor valor de faturamento: {menor_diaria}")
print(f"Maior valor de faturamento: {maior_diaria}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
