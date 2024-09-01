## Justificativa

Escolhi a linguagem de programação Python devido à sua simplicidade e à eficiência das suas bibliotecas, que facilitam a implementação da leitura de dados e a clareza do código.

### Bibliotecas Utilizadas

- **`json`**: Utilizada para leitura de arquivos JSON nas questões 3 e 4.

A seguir, apresento a resolução das questões propostas.

## Questões Resolvidas

### 1. Cálculo da Soma

Considere o seguinte trecho de código:

```plaintext
int INDICE = 13, SOMA = 0, K = 0; 
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA); 
```
## Ao final do processamento, qual será o valor da variável SOMA? 

### Resposta

O valor final da variável \`SOMA\` será 91.

## 2. Verificação de Pertencimento à Sequência de Fibonacci

Implementação para verificar se um número pertence à sequência de Fibonacci.

#### Resposta

Veja a implementação em: [questao2/fibonacci.py](questao2/fibonacci.py)

## 3. Análise de Faturamento Mensal

Para um arquivo JSON contendo dados de faturamento diário, foram realizados os seguintes cálculos:

- Maior faturamento do mês
- Menor faturamento do mês
- Número de dias em que o faturamento diário superou a média

#### Resposta

Veja a implementação em: [questao3/faturamento_mes.py](questao3/faturamento_mes.py)

## 4. Percentual de Representação de Cada Estado

Para um arquivo JSON com dados de faturamento por estado, foram realizados os seguintes cálculos:

- Leitura do arquivo JSON
- Cálculo do total de faturamento
- Cálculo do percentual de faturamento para cada estado

#### Resposta

Veja a implementação em: [questao4/faturamento_estados.py](questao4/faturamento_estados.py)

## 5. Reversão de String

Implementação para reverter uma string sem utilizar funções prontas para esse fim.

#### Resposta

Veja a implementação em: [questao5/reverse.py](questao5/reverse.py)